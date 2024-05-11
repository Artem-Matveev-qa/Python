import requests
import pytest

URL = 'https://api.pokemonbattle-stage.me/v2'
TOKEN = '8f55ba4a3411ecece922744b221dfc76'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 992


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_name():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.json()['data'][0]['trainer_name'] == 'ARTIK'
   