from omdb_api_lib import Omdb

import os
import json
from dotenv import load_dotenv

def load_api_key():
    try:
        load_dotenv()
        return os.getenv("API_KEY")
    except Exception as e:
        print('ERROR >>>>', e)
        exit()

def format_result(req):
    
    movie_info = json.loads(req.text)

    if movie_info.get('Response') == 'True':
        print('')
        print('Titulo: ', movie_info['Title'])
        print('Ano: ', movie_info['Year'])
        print('Diretor: ', movie_info['Director'])
        print('Atores: ', movie_info['Actors'])
        print('Nota: ', movie_info['imdbRating'])
    else: 
        print('Não encontrado.')

def main():

    api_key = load_api_key()

    omdb_api = Omdb()
    
    movie_name = str(input('Digite o filme que deseja buscar: '))

    

    result = omdb_api.search_movie_rating(movie_name)

    format_result(result)

main()