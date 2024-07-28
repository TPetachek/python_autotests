import requests
# {'id': '4265', 'trainer_token': '', 'trainer_name': 'Акаша'}
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '073cb5ee6480ed4753ab979fdba4827f'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

# Создаем покемона - боди
body_pokemon_create = {
    "name": "Pythomon",
    "photo_id": 1
}

# Создаем покемона - запрос
response_pokemon_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon_create)
print (response_pokemon_create.text)
pokemon_id = response_pokemon_create.json()['id']

# Переименовываем покемона - боди
body_pokemon_rename = {
    "pokemon_id": pokemon_id,
    "name": "Renamed Pythomon",
    "photo_id": 2
}

# Ловим покемона - боди
body_pokemon_catch = {
    "pokemon_id": pokemon_id
}

# Переименовываем покемона - запрос
response_pokemon_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon_rename)
print (response_pokemon_rename.text)

# Ловим покемона - запрос
response_pokemon_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemon_catch)
print (response_pokemon_catch.text)