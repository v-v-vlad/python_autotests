import requests

URL = 'https://api.pokemonbattle.ru/v2/'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : '420b998981a93a6bd0c5a4ec3baadf38'}
photo_id_auto = 960
name_pokemon_auto = 'Питон'
new_name_pokemon_auto = 'New Питон'

print('# 1 Создание покемона')
# 1 Создание покемона
body_create_pokemon = {
    "name": name_pokemon_auto,
    "photo_id": photo_id_auto
}
response = requests.post(url = f'{URL}pokemons', headers= HEADER, json=body_create_pokemon)
print(response.status_code)
print(response.text)

pokemon_id = response.json()['id']

print('# 2 Cмена имени покемона')
# 2 Cмена имени покемона
body_new_name_pokemon = {
    "pokemon_id": pokemon_id,
    "name": new_name_pokemon_auto,
    "photo_id": photo_id_auto
}
response = requests.put(url = f'{URL}pokemons', headers= HEADER, json=body_new_name_pokemon)
print(response.status_code)
print(response.text )

print('# 3 Поймать покемона в покебол')
# 3 Поймать покемона в покебол
body_catch_pokemon = {
    "pokemon_id": pokemon_id
}
response = requests.post(url = f'{URL}trainers/add_pokeball', headers= HEADER, json=body_catch_pokemon)
print(response.status_code)
print(response.text)

print('# Доп этап: нокаут нового покемона')
# Доп этап: нокаут нового покемона
body_knockout_pokemon = {
    "pokemon_id": pokemon_id
}
response = requests.post(url = f'{URL}pokemons/knockout', headers= HEADER, json=body_knockout_pokemon)
print(response.status_code)
print(response.text )
