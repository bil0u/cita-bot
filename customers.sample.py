from bcncita import DocType, Province, Office, OperationType


# All values filled here will be propagated to all customers
DEFAULTS = {
    'offices': [
        Office.BARCELONA,
        Office.BARCELONA_MALLORCA,
    ]
}

# List of all the customers to process
# For details of how to fill all the fields, see the documentation here : ./docs/customers.md
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
