import requests

class Omdb:

    api_key = None
    
    def __init__(self):
        pass

    def search_movie_rating(self, movie_name):
        try:
            if not self.api_key:
                raise ValueError("A chave de API não foi configurada.")
            api_adress = f'https://www.omdbapi.com/?t={movie_name}&apikey={self.api_key}' 
            result = requests.post(api_adress)
            return result
        except Exception as e:
            print('ERROR >>>>', e)
            exit()

    def set_api_key(self, api_key):
        try:
            self.api_key = api_key
        except Exception as e:
            print('ERROR >>>>', e)
            exit()