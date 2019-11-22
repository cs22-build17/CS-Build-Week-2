import requests

headers = {
        'Authorization': f"Token 7922ffc0cc5d060b72e31aa06131cddc3b7775f7",
        'Content-Type': 'application/json',
    }

init_response = requests.get(
    'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers)
init_data = init_response.json()
room_id = init_data['room_id']
exits = init_data['exits']



# world_map = { {0: {n: 10, s: 9}}, 1: {e: 10, w: 9}},  }
world_map = {}
dictionary_entry = {}
# dictionary_entry[2] = (70, 90)

for exit in exits: 
    dictionary_entry[exit] = "?"
    world_map[room_id] = dictionary_entry
    world_map[room_id]['n'] = 1
print(world_map)





# print(dictionary_entry)

# world_map.append(dictionary_entry) 

# print('world map', world_map)


