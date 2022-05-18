# Setup

## Homebrew - macOS only

1. Install [homebrew](https://brew.sh/index_fr)
2. With homebrew, Install the following:
   - **pipenv** : `brew install pipenv`
   - **google-chrome** : `brew install --cask google-chrome`
   - **chomedriver** : `brew install --cask chromedriver`

## Classical - Any OS

1. Install [Python 3.8](https://www.python.org/downloads/release/python-385/).
2. `pip install -r requirements.txt`
3. Install Google Chrome.
4. Download [chromedriver](https://chromedriver.chromium.org/downloads) and put it in the PATH (Python dir from step 1 should work).
   4.1. [Windows only] Download [wsay](https://github.com/p-groarke/wsay/releases) and put it in the PATH.

## Automation - Optional

You can create a file named `.env` to provide extra configuration to the bot. See the [`.env.sample`](../.env.sample) file for reference.

1. Get API key from https://anti-captcha.com, and set it as `ANTICAPTCHA_API_KEY` in `.env`.
2. Get API key from https://webhook.site and set it as `SMS_WEBHOOK_TOKEN` in `.env`.
3. Install [IFTTT](https://ifttt.com/) or any other automation tool on your phone and create an applet redirecting SMS having text `CITA PREVIA` to the temporary email you got from https://webhook.site.
