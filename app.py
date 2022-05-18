from genericpath import exists
import os
from pathlib import Path
import sys
import hashlib, base64

from bcncita import CustomerProfile, try_cita
from dotenv import dotenv_values

try:
    from customers import DEFAULTS, CUSTOMERS
except ImportError:
    raise Exception("You must define customers.py. See")


env = dotenv_values('.env')

CONFIG = {
    'anticaptcha_api_key': env.get('ANTICAPTCHA_API_KEY', None),
    'auto_captcha': 'ANTICAPTCHA_API_KEY' in env,
    'auto_office': True,
    'chrome_driver_path': env.get('CHROME_DRIVER_PATH', '/usr/local/bin/chromedriver'),
    'chrome_profile_name': env.get('CHROME_PROFILE_NAME', None),
    'chrome_profile_path': env.get('CHROME_PROFILE_PATH', None),
    'save_artifacts': False,
    'sms_webhook_token': env.get('SMS_WEBHOOK_TOKEN', None),
    'wait_exact_time': None,
}

def create_customer(**details):
    """ Create a customer profile """
    return CustomerProfile(
        **CONFIG,
        **DEFAULTS,
        **details
    )

def run(customer):
    """ Classic run """
    try_cita(context=customer, cycles=200)  # Try 200 times


def run_autofill(customer):
    """ Autofill for chrome """
    from mako.template import Template

    tpl = Template(
        filename=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "bcncita/template/autofill.mako"
        )
    )
    print(tpl.render(ctx=customer))

def get_hash(value):
    return base64.urlsafe_b64encode(hashlib.md5(value.encode()).digest()).decode('ascii')


if __name__ == "__main__":

    print('Bot activity started.')

    # Reading history file
    history_path = Path('history.txt')
    history_path.touch(exist_ok=True)
    with open(history_path) as f:
        history = f.readlines()

    # Getting appropriate function
    func = run_autofill if "--autofill" in sys.argv else run

    for details in CUSTOMERS:
        
        customer = create_customer(**details)
        hash =  get_hash(customer.doc_type + customer.doc_value) + '\n'

        if hash in history:
            print(f'Ignoring {customer.doc_value}')
            continue

        try:
            func(customer)
            history.append(hash)
        except KeyboardInterrupt:
            break

    
    # Overriding history
    with open(history_path, 'w') as f:
        f.writelines(history)
        
            
    print('Bot activity ended.')
