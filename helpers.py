import json
from io import StringIO

""" Data for use in mocking """

get_brands_response = """
{
  "meta": {
    "limit": 10,
    "next": null,
    "offset": 0,
    "previous": null,
    "total_count": 3
  },
  "objects": [
    {
      "id": 1,
      "id_externo": null,
      "nome": "Marca de produto",
      "apelido": "marca",
      "descricao": "Descrição detalhada da marca",
      "imagem": null,
      "resource_uri": "/api/v1/marca/1"
    },
    {
      "id": 2,
      "id_externo": null,
      "nome": "Marca de produto 2",
      "apelido": "marca-2",
      "descricao": "Descrição detalhada da marca 2",
      "imagem": "http://www.lojaintegrada.com.br/1/marca/1/g/90cd6b495e.jpg",
      "resource_uri": "/api/v1/marca/2"
    },
    {
      "id": 3,
      "id_externo": 4,
      "nome": "Marca de produto 3",
      "apelido": "marca-3",
      "descricao": "Descrição detalhada da marca 3",
      "imagem": null,
      "resource_uri": "/api/v1/marca/4?id_externo=1"
    },
    {
      "id": 4,
      "id_externo": 5,
      "nome": "Marca de produto 4",
      "apelido": "marca-4",
      "descricao": "Descrição detalhada da marca 4",
      "imagem": null,
      "resource_uri": "/api/v1/marca/5?id_externo=1"
    }
  ]
}
"""

customer_create_response = """
{
  "aceita_newsletter": true,
  "cnpj": null,
  "cpf": "37363337144",
  "data_criacao": "2014-04-04 13:48:49.689375",
  "data_modificacao": "2014-04-04 13:48:49.689413",
  "data_nascimento": "1980-01-01",
  "email": "joao@exemplo.com.br",
  "enderecos": [
    {
      "bairro": "Freg. do Ó",
      "cep": "02960030",
      "cidade": "São Paulo",
      "cliente": "/api/v1/cliente/103265/",
      "complemento": "Apartamento 32",
      "endereco": "Rua das Flores",
      "estado": "SP",
      "id": 13144,
      "nome": "Jonatas Oliveira",
      "numero": "123",
      "pais": "Brasil",
      "principal": true,
      "referencia": "",
      "resource_uri": "/api/v1/endereco/102512/"
    }
  ],
  "grupo": {
    "id": 1,
    "nome": "Padrão",
    "padrao": true,
    "resource_uri": "/api/v1/grupo/1/"
  },
  "id": 1,
  "ie": null,
  "newsletter": false,
  "nome": "João Exemplo",
  "razao_social": null,
  "resource_uri": "/api/v1/cliente/1/",
  "rg": "123456-7",
  "sexo": "m",
  "telefone_celular": "11999998888",
  "telefone_comercial": "1140620137",
  "telefone_principal": "1133334444",
  "tipo": "PF"
}
"""

mock_customer_response = json.loads(customer_create_response)
mock_brands_response = json.loads(get_brands_response)

in_mem_csv = StringIO(
    (
        'email,_website,_store,confirmation,created_at,created_in,dob,'
        'firstname,gender,group_id,inscription_pj,inscription_pj_uf,is_pj,'
        'lastname,middlename,name_fantasy,password_hash,pf_rg,prefix,rp_token,'
        'rp_token_created_at,social_reason,store_id,suffix,taxvat,website_id,'
        'password,_address_city,_address_company,_address_country_id,'
        '_address_fax,_address_firstname,_address_lastname,_address_middlename,'
        '_address_postcode,_address_prefix,_address_region,_address_street,'
        '_address_suffix,_address_telephone,_address_default_billing_,'
        '_address_default_shipping_'
        '\n'
        'daniel.drbike@gmail.com,base,default,,2010-05-23 14:05:21,'
        'Ciclo Urbano,,Daniel,,1,,,,Rodrigues,,,'
        'ed32fd4eef628a5d760e8e80fd53d3f8:Wc,,,,,,1,,,1,,,,,,,,,,,,,,,,,'
        '\n'
        'leandrovalverdes@gmail.com,base,default,,2010-05-31 19:07:27,'
        'Ciclo Urbano,,Leandro ,,1,,,,Valverdes,,,'
        '97f8cbea14cd5921f075e238ce029475:NN,,,,,,1,,280.247.388-30,1,,'
        'SAO PAULO,,BR,,Leandro ,Valverdes,,04012-002,,São Paulo,'
        'RUA PELOTAS\n'
        'Vila Mariana\n'
        '523\n'
        '81",,(11)5548-2162,1,1,'
    )
)

br_states = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}
