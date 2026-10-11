# Nessa aula aprendemos a instalar pacotes via PIP no python, para isso instalamos a biblioteca 'requests', que traz funcoes para 
# o envio de http requests. Veja nó cpodigo abaixo:

import requests

# GET

print('\nGET\n')

try:
    requisicao = requests.get('https://facebook.com.br')
    print('Status Code: ',requisicao.status_code)
except Exception as e:

    print('Erro >>>',e )

# POST

print('\nPOST\n')

header = {
    'User-agent': 'Windows 50',
    'Referer': "https://google.com",
    'cf-ipcountry': 'US'
}

cookies = {
    'Ultima-visita': '10-10-2020'
}

data= {
    'username': 'eli',
    'password': ''

}

try:
    
    req = requests.post('https://putsreq.com/urooDpwzwCC835OO68uU', headers=header, cookies=cookies, data=data)
    
    print('Status Code: ',req.status_code)

    print('Response: ',req.text)
except Exception as e:
    print('Error >>>', e)

