import csv
from helpers import br_states

headers_li = [
    'email', 'nome', 'sexo', 'aceita_newsletter', 'telefone_principal',
    'telefone_comercial', 'telefone_celular', 'grupo_id', 'tipo', 'cpf', 'rg',
    'razao_social', 'cnpj', 'ie', 'endereco', 'numero', 'complemento', 'bairro',
    'cidade', 'estado', 'cep', 'pais', 'nome', 'data_nascimento'
]


def find_state(state_full_name: str) -> str | None:
    """ Given a brazilian state full name, return its initials """
    for initial, state_name in br_states.items():
        if state_name == state_full_name:
            return initial
    # Returns None if no initials are found
    return None


def filter_adddress(address: str) -> dict[str, str] | None:
    """
    From a string representing an address, classify into subcomponents
    such as street name, number, district, additional information
    Returns a dict with the information above
    """
    # If an empty string is provived, return None
    if not address:
        return None

    # Splits the address data into a list
    address = address.split('\n')
    result = dict.fromkeys(
        ['street', 'street_num', 'district', 'complemento'],
        ''
    )

    # The first item will always be the street name
    result['street'] = address.pop(0)

    found_street_number = False
    found_district = False
    for data in address:
        # If it's an empty string, pass
        if not data:
            continue
        # Remove unwanted leading or trailing spaces
        data = data.strip()
        # If composed by letters and spaces and is after address, is district
        if all(x.isalpha() or x.isspace() for x in data) and not found_district:
            if result['district']:
                result['district'] += f' - {data}'
            else:
                result['district'] += data
            found_district = True
        # If first characters is a number, probably a street number
        elif data[0].isnumeric() and not found_street_number:
            if result['street_num']:
                result['street_num'] += f' - {data}'
            else:
                result['street_num'] += data
            found_street_number = True
        # If another number is found, probably is apartment number
        elif data.isnumeric() and found_street_number:
            if result['complemento']:
                result['complemento'] += f' - {data}'
            else:
                result['complemento'] += data
        else:
            if result['complemento']:
                result['complemento'] += f' - {data}'
            else:
                result['complemento'] += data

    return result


with open('result.csv', 'w') as output_file:
    with open('customers.csv', 'r') as input_file:
        csv_reader = csv.DictReader(input_file, delimiter=',')
        csv_writer = csv.DictWriter(output_file, fieldnames=headers_li)

        csv_writer.writeheader()
        for row in csv_reader:
            # If it is a invalid user row, pass
            if row['email'] == '':
                continue

            address = filter_adddress(row['_address_street'])
            if address is None:
                continue

            csv_writer.writerow({
                'email': row['email'],
                'nome': f"{row['firstname']} {row['lastname']}",
                'sexo': '',
                'aceita_newsletter': '',
                'telefone_principal': row['_address_telephone'],
                'telefone_comercial': '',
                'telefone_celular': '',
                'grupo_id': 1,
                'tipo': 'PF',
                'cpf': row['taxvat'],
                'rg': '',
                'razao_social': '',
                'cnpj': '',
                'ie': '',
                'endereco': address['street'],
                'numero': address['street_num'],
                'complemento': address['complemento'],
                'bairro': address['district'],
                'cidade': row['_address_city'],
                'estado': find_state(row['_address_region']),
                'cep': row['_address_postcode'],
                'pais': 'BRA',
                'data_nascimento': '',
            })
