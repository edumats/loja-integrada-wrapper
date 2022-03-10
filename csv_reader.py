import sys
import csv
from typing import Union

from helpers import br_states

headers_li = [
    'email', 'nome', 'sexo', 'aceita_newsletter', 'telefone_principal',
    'telefone_comercial', 'telefone_celular', 'grupo_id', 'tipo', 'cpf', 'rg',
    'razao_social', 'cnpj', 'ie', 'endereco', 'numero', 'complemento', 'bairro',
    'cidade', 'estado', 'cep', 'pais', 'nome', 'data_nascimento'
]


def find_state(state_full_name: str) -> Union[str, None]:
    """ Given a brazilian state full name, return its initials """
    for initial, state_name in br_states.items():
        if state_name == state_full_name:
            return initial
    # Returns None if no initials are found
    return None


def filter_adddress(address: str) -> Union[dict[str, str], None]:
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
        ['street', 'street_num', 'district', 'complement'],
        ''
    )

    # The first item will always be the street name
    result['street'] = address.pop(0)

    found_street_number = False
    found_district = False
    # Iterate over each item of address list
    for data in address:
        # If it's an empty string, pass
        if not data:
            continue
        # Remove unwanted leading or trailing spaces
        data = data.strip()
        # If composed by letters and spaces and is after address, is district
        if all(char.isalpha() or char.isspace() for char in data) and not found_district:
            if result['district']:
                result['district'] += f' - {data}'
            else:
                result['district'] += data
            found_district = True
        # If first character is a number, probably a street number
        elif data[0].isnumeric() and not found_street_number:
            if result['street_num']:
                result['street_num'] += f' - {data}'
            else:
                result['street_num'] += data
            found_street_number = True
        else:
            if result['complement']:
                result['complement'] += f' - {data}'
            else:
                result['complement'] += data

    return result


def main():
    if len(sys.argv) != 3:
        sys.exit('Usage: python csv.reader.py input_file output_file')

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Opens output file and input file
    with open(output_file, 'w') as output:
        with open(input_file, 'r') as input:
            csv_reader = csv.DictReader(input, delimiter=',')
            csv_writer = csv.DictWriter(output, fieldnames=headers_li)

            csv_writer.writeheader()
            for row in csv_reader:
                # If it is a invalid user row, pass
                if row['email'] == '':
                    continue

                print(repr(row['_address_street']))
                address = filter_adddress(row['_address_street'])
                if address is None:
                    continue

                # Convert to all elements of names starting with capital letter
                first_name = row['firstname'].title()
                last_name = row['lastname'].title()

                csv_writer.writerow({
                    'email': row['email'],
                    'nome': f"{first_name} {last_name}",
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
                    'complemento': address['complement'],
                    'bairro': address['district'],
                    'cidade': row['_address_city'],
                    'estado': find_state(row['_address_region']),
                    'cep': row['_address_postcode'],
                    'pais': 'BRA',
                    'data_nascimento': '',
                })


if __name__ == '__main__':
    main()
