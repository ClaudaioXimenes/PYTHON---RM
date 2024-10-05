import requests
from requests.auth import HTTPBasicAuth

# Definindo a URL da API
url = "http://localhost:8051/api/rh/v1/employeeDataContent?product=RM&companyId=1"

# Definindo as credenciais
username = "mestre"
password = "totvs"

# Realizando a requisição com autenticação Basic
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Exibindo o retorno da requisição
if response.status_code == 200:
    print("Dados recebidos:")
    data = response.json()  # Se o retorno for JSON

    # Acessando a lista de funcionários na chave 'items'
    if 'items' in data:  # Verifica se a chave 'items' está presente
        for employee in data['items']:
            print(f"A chapa do funcionárioé: {employee['code']}")  # Acessando e exibindo a chapa do funcionário
            print(f"O nome do funcionário é: {employee['name']}") # Acessando e exibindo o nome do funcionário
            print(F"A data de admissão é: {employee['hiringDate']}") # Acessando e exibindo a admissão do funcionário
    else:
        print("Nenhum item encontrado na resposta.")
else:
    print(f"Erro {response.status_code}: {response.text}")