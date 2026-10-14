import requests
import json
import os

def load_api_key():
    try:
        return os.environ["OPENWEATHER_KEY"]
    except Exception as e:
        print('ERROR >>>>', e)
        exit()

api_key = '821d836560bbc83226a75b28f38fb2dc'

city_name = str(input('Qual cidade deseja saber o clima? \n'))

api_url = f'https://api.openweathermap.org/data/4.0/weather?q={city_name}&appid={api_key}'

req = requests.get(api_url)

print(json.loads(req.text))