# Cita Helper !

_Forked from [this project](https://github.com/cita-bot/cita-bot)_

This Selenium automatization script helps to catch cita timeslot for Spanish CNP/Extranjería.

Enable your speakers and wait for "ALARM ALARM ALARM" message :) Next you'll have to confirm an appointment via SMS code.

It can make a reservation automatically if you set up anti-captcha, webhooks and IFTTT applet on your phone, read instructions below.

## Documentation

- [Setup](./docs/setup.md)
- [Customers](./docs/customers.md)
- [Development](./docs/development.md)
- [Troubleshooting](./docs/troubleshooting.md)

## Regular use

1. Fill your customer data in `customers.py`. See [documentation](./docs/customers.md)
2. Eventually update chrome and webdrivers using `pipenv run setup:update`
3. Run `pipenv run start` or `pipenv run start:autofill`, and follow the voice instructions.
