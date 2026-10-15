


# devido ao fato de que na epoca do curso o Twitter ainda não tinha se tornado o X o método descrito funciona apenas na aula.

# Nos dias de hoje requer varias alterações para se obter um result da api. No codigo abaixo eu fiz algumas alteracoes 
# para que se obtivesse algum resultado, porem para que se possa obter esse resultado é necessario pagar pela chamada de api.


from dotenv import load_dotenv
import requests
import os
import json

consumer_key = None
secret_key = None
bearer_token = None

def set_up_env():
    try:
        global bearer_token
        load_dotenv()
        bearer_token = str(os.getenv('BEARER_TOKEN'))

        if not bearer_token:
            raise ValueError("BEARER_TOKEN não foi configurado.")

    except Exception as e:
        print('Error >>>>', e)
        exit()

set_up_env()


def request_to_api(query):
    try:
        
        api_url = 'https://api.x.com/2/tweets/search/recent'

        headers = {
            "Authorization": f"Bearer {bearer_token}"
        }

        params = {
            "query": query,
            "max_results": 10
        }

        response = requests.get(api_url, headers=headers, params=params, timeout=15)

        response.raise_for_status()


        return response.json()
    
    except Exception as e:
        print('Error >>>>', e)
        exit()

data = request_to_api('brasil')

fromated_data = json.dumps(data, indent=4)

for post in fromated_data.get("data", []):
    print(post["text"])

