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
    print(response.json())  # Se o retorno for JSON
else:
    print(f"Erro {response.status_code}: {response.text}")