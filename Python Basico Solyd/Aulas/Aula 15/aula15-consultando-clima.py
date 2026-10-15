import requests
import json
import os
from dotenv import load_dotenv

def load_api_key():
    try:
        load_dotenv()
        return os.getenv("OPENWEATHER_KEY")
    except Exception as e:
        print('ERROR >>>>', e)
        exit()

api_key = load_api_key()

city_name = str(input('Qual cidade deseja saber o clima? \n'))

api_url = f'https://api.openweathermap.org/data/4.0/weather?q={city_name}&appid={api_key}'

req = requests.get(api_url)

print(json.loads(req.text))