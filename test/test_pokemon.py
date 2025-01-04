import requests
import pytest
URL = 'https://api.pokemonbattle.ru/v2/'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : '420b998981a93a6bd0c5a4ec3baadf38'}


def test_response_code():
    response = requests.get(url = f'{URL}trainers', headers= HEADER)
    assert response.status_code == 200

def test_response_name_trainer():
    response = requests.get(url = f'{URL}trainers',params = {'trainer_id': '14993'} , headers= HEADER)
    assert response.json()['data'][0]['id'] == '14993'


@pytest.mark.parametrize('key,value',[('id', '14993'),("trainer_name","VvVlad"),("level","5")])
def test_parametrize(key, value):
    response = requests.get(url = f'{URL}trainers',params = {'trainer_id': '14993'} , headers= HEADER)
    assert response.json()['data'][0][key] == value

