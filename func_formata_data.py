import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import dateutil.parser

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
            print(f"A chapa do funcionário é: {employee['code']}")  # Acessando e exibindo a chapa do funcionário  employees.costCenterDescription
            print(f"O nome do funcionário é: {employee['name']}") # Acessando e exibindo o nome do funcionário
                     
            # Convertendo a data de admissão para o formato DD/MM/YYYY
            hiring_date = dateutil.parser.parse(employee['hiringDate'])
            formatted_date = hiring_date.strftime('%d/%m/%Y')
            
            print(f"A data de admissão é: {formatted_date}") # Exibindo a data de admissão formatada
            print(f"O seu Centro de Custo é: {employee['costCenterDescription']}") 
            print(f"O seu Departamento é: {employee['departmentDescription']}") 
            print("-" * 90)  # Linha separadora para melhor visualização
    else:
        print("Nenhum item encontrado na resposta.")
else:
    print(f"Erro {response.status_code}: {response.text}")