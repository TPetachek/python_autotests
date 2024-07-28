import pytest
import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '073cb5ee6480ed4753ab979fdba4827f'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '4265'

trainer_name = 'Акаша'

def test_status_code():
    response = requests.get(url= f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_id():
    response_id = requests.get(url= f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_id.json()["data"][0]["trainer_name"] == trainer_name


# @pytest.mark.parametrize('key, value', [('trainer_name', 'Акаша'), ('id', TRAINER_ID), ('level', '1')])
# def test_trainer_level(key, value):
#     response_level = requests.get(url= f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
#     assert response_level.json()["data"][0][key] == value    