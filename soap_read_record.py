from zeep import Client
from zeep.transports import Transport
import requests
from requests.auth import HTTPBasicAuth

# Endereço WSDL do web service SOAP
wsdl = 'http://localhost:8051/wsDataServer/MEX?wsdl'

# Credenciais de autenticação
username = 'mestre'
password = 'totvs'

# Criar sessão para o transporte com autenticação Basic
session = requests.Session()
session.auth = HTTPBasicAuth(username, password)

# Transport com a sessão e autenticação
transport = Transport(session=session)

# Criar o cliente SOAP
client = Client(wsdl, transport=transport)

# Parâmetros do método ReadRecord
data_server_name = 'GlbUsuarioData'  # Nome do DataServer
primary_key_value = 'mestre'  # Chave primária que você deseja buscar
contexto = 'CODSISTEMA=G;CODCOLIGADA=0;CODUSUARIO=mestre'  # Contexto adicional

# Chamar o método ReadRecord com os parâmetros
response = client.service.ReadRecord(data_server_name, primary_key_value, contexto)

# Exibir a resposta
print(response)