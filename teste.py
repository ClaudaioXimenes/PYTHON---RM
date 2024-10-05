import requests
from requests.auth import HTTPBasicAuth

# URL do serviço SOAP (verifique se essa é a URL correta do seu endpoint)
url = "http://localhost:8051/wsDataServer/MEX"  # Ajuste se necessário

# Cabeçalhos HTTP
headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': 'http://www.totvs.com/ReadRecord'  # Ajuste o SOAPAction se necessário
}

# Envelope SOAP
soap_envelope = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tot="http://www.totvs.com/">
   <soapenv:Header/>
   <soapenv:Body>
      <tot:ReadRecord>
         <tot:DataServerName>GlbUsuarioData</tot:DataServerName>
         <tot:PrimaryKey>mestre</tot:PrimaryKey>
         <tot:Contexto>CODSISTEMA=G;CODCOLIGADA=0;CODUSUARIO=mestre</tot:Contexto>
      </tot:ReadRecord>
   </soapenv:Body>
</soapenv:Envelope>"""

# Credenciais para autenticação Basic
username = 'mestre'
password = 'totvs'

# Enviar a requisição POST com o envelope SOAP e autenticação
response = requests.post(url, data=soap_envelope, headers=headers, auth=HTTPBasicAuth(username, password))

# Exibir a resposta do servidor
print("Status Code:", response.status_code)
print("Response Text:", response.text)