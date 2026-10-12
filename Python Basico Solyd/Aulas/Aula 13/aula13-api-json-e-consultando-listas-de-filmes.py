
import os
import requests
import json

def load_api_key():
    try:
        return os.environ["API_KEY"]
    except Exception as e:
        print('ERROR >>>>', e)
        exit()

def ask_movie():
    try:
        movie_title = str(input('\nQual filme deseja buscar? '))
        return movie_title
    except Exception as e:
        print('ERROR >>>>',e)

def make_req(api_key, movie_title):
    try:
        api_adress = f'https://www.omdbapi.com/?t={movie_title}&apikey={api_key}'
        req = requests.post(api_adress)
        return req
    except Exception as e:
        print('ERROR >>>>', e)
        exit()
        

def gen_answer(req):
    
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

    while True:

        movie_title = ask_movie()

        req = make_req(api_key,movie_title)

        gen_answer(req)

main()