import requests
import json
import time

api_url = 'https://economia.awesomeapi.com.br/json/last/'

req = requests.get(f'{api_url}USD,BTC')

cotations = json.loads(req.text)

def print_cotation(cotation: json):
    cota = cotations[cotation]
    print(f'\n{cota["name"]}')
    print(' Preço de Compra: ', float(cota["ask"])/10000)
    print(' Preço de Venda:  ', float(cota["bid"])/10000)

while True:
    for cot in cotations:
        print_cotation(cot)

    print('\n')
    dot = ''
    for i in range(4):
        time.sleep(1)
        dot += '.'
        print('Atualizando',dot, end='\r', flush=True)

    print('')