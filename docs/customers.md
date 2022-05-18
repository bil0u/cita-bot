# Customers

In order for the bot to work, you have to create a file named `customers.py` in the [main directory](./..), containing a dictionnary `DEFAULTS`, and a list `CUSTOMERS`. You can duplicate `customers.sample.py` as a starter.

The file content should look like this:

```python
from bcncita import DocType, Province, Office, OperationType

DEFAULTS = {
    'offices': [
        Office.BARCELONA,
        Office.BARCELONA_MALLORCA,
    ]
}

CUSTOMERS = [
    {
        # Procedure details
        'operation_code': OperationType.CERTIFICADOS_UE,
        'doc_type': DocType.PASSPORT,
        'province': Province.BARCELONA,
        'reason_or_type': None,
        # Customer details
        'doc_value': '12AB01234',
        'name': 'John Doe',
        'year_of_birth': '1990',
        'phone': '612345678',
        'email': 'johndoe@domain.tld',
        'country': "FRANCIA",
        # Appointment details
        'min_date': '01/01/2022',
        'max_date': '31/12/2022',
        'card_expire_date': None,
        # 'offices': [],
        # 'except_offices': [],
    }
]
```

##### DEFAULTS

All fields in this dictionnary will be propagated to all customers.
In the example, we use it to take appointments in two offices only.

To disable it, set to an empty dictionnary

```python
DEFAULTS = {}
```

##### CUSTOMERS

A list containing dictionnaries, each dictionnary describes a customer to take an appointment for.

Here are the list of avaiable properties

###### Procedure details

- `operation_code` — Procedure. See [full list](../bcncita/cita.py#L46).
- `doc_type` — Document type. See [full list](../bcncita/cita.py#L40).
- `province` — Province name. See [full list](../bcncita/cita.py#L94).
- `reason_or_type` — "Motivo o tipo de solicitud de la cita". Required for some cases, like `OperationType.SOLICITUD_ASILO`. See [related blog post](https://blogextranjeriaprogestion.org/2018/05/14/cita-previa-tramites-asilo-pradillo/).

###### Customer details

- `doc_value` — Document number, no spaces
- `name` — First and Last Name
- `year_of_birth` — Year of birth, like "YYYY"
- `phone` — Phone number, no spaces, like "600000000"
- `email` — Email
- `country` — Country (`FRANCIA` by default). Copypaste yours from the appropriate page.

###### Appointment details

- `min_date` — Minimum date for appointment in "dd/mm/yyyy" format. Appointments available earlier than this date will be skipped.
- `max_date` — Maximium date for appointment in "dd/mm/yyyy" format. Appointments available later than this date will be skipped.
- `card_expire_date` — Card Expiration Date. Probably, it's not important at all, leave it empty.
- `offices` — Required field for `OperationType.RECOGIDA_DE_TARJETA`! If provided, script will try to select the specific police station or end the cycle. For `OperationType.TOMA_HUELLAS` it attempts to select all provided offices one by one, otherwise selects a random available. See [supported offices](../bcncita/cita.py#L59).
- `except_offices` — Select offices you would NOT like to get appointment at.
