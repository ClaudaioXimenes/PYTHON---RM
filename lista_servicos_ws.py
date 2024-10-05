from zeep import Client

# Endereço WSDL do seu web service SOAP
wsdl = 'http://localhost:8051/wsDataServer/MEX?wsdl'

# Criar um cliente SOAP
client = Client(wsdl)

# Listar os métodos/serviços disponíveis
for service in client.wsdl.services.values():
    for port in service.ports.values():
        operations = port.binding._operations
        for operation in operations:
            print(operation)