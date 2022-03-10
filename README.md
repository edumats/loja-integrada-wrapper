# Loja Integrada's Wrapper

## Introduction

This is a Python based wrapper for Loja Integradas's API. It is possible to use the API paths without dealing with implementation details as API's rate limits or the Python's requests module.

The rate limiting is managed by the [ratelimit](https://pypi.org/project/ratelimit/) module and the maximum number of requests is set at 100 calls/minute (the maximum allowed calls, according to the [Loja Integradas's official documentation](https://lojaintegrada.docs.apiary.io)). If one tries to make more calls than the maximum limit, the wrapper will sleep and retry after a minute is elapsed, ensuring that all calls to the API are successful.

Based on Loja Integradas's API documentation:
[Loja Integrada's API docs](https://lojaintegrada.docs.apiary.io)

## How to use

It is necessary to obtain the APP KEY (chave da API) and the API KEY (chave da aplicação) from Loja Integrada. The APP KEY can be easily obtained from Loja Integrada's admin pannel, but the API KEY must be requested from the Loja Integrada's tech support. Note that it is necessary to have a Loja Integrada's PRO plan to be able to obtain both of these keys.

Set the environment variables APP_KEY and API_KEY on your environment

On Linux or MacOS:

```
export APP_KEY=<APP KEY>
export API_KEY=<API_KEY>
```

Example of wrapper usage

```
# Imports the wrapper class
from wrapper import LojaIntegrada as LI

# Instantiates the wrapper object
wrapper = LI()

# Calls the API and creates a new customer
wrapper.create_customer(key1=value1, key2=value2) `
```

## Available methods

# create_customer()

If request is successful, returns a dict with the following content:

```
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
```
