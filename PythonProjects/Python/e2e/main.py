import requests 

URL = 'https://api.pokemonbattle-stage.me/v2'
TOKEN = '8f55ba4a3411ecece922744b221dfc76'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Чаризард",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
}

body_change = {
    "pokemon_id": "3155",
    "name": "Пикачу",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_pokebol = {
    "pokemon_id": "3155"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)''' 

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_pokebol = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokebol)
print(response_pokebol.text)
