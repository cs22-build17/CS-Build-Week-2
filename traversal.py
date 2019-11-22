import requests
import time
from stack_and_queue import Queue

def traverseMap():
    headers = {
        'Authorization': f"Token 7922ffc0cc5d060b72e31aa06131cddc3b7775f7",
        'Content-Type': 'application/json',
    }
    
    unused_exits = {}
    backtrack_path = []
    world_map = {}
    dictionary_entry = {}

    reversed_dir = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
    init_response = requests.get(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers)
    init_data = init_response.json()
    # current_room = init_data['title']
    room_title = init_data['title']
    room_id = init_data['room_id']
    print('initial room id', room_id)
    cd = init_data['cooldown']
    coordinates = init_data['coordinates']
    room_exits = init_data['exits']

    for exit in room_exits: 
        dictionary_entry[exit] = "?"
        world_map[room_id] = dictionary_entry
    print(world_map)


    unused_exits[room_id] = room_exits
    print('cd', cd)
    time.sleep(cd + 1)
    direct = {}


    while len(unused_exits) < 499:
        
        if room_id not in unused_exits:
            unused_exits[room_id] = room_exits
            previous_dir = backtrack_path[-1]
            unused_exits[room_id].remove(previous_dir)


        while len(unused_exits[room_id]) == 0:
            previous_dir = backtrack_path.pop()
            direct['direction'] = str(previous_dir)

            old_room_id = room_id
            print('old_room_id...........', old_room_id)

            move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=direct)
            json_response = move_response.json()
            room_id = json_response['room_id']
            room_exits = json_response['exits']
            room_title = json_response['title']
            coordinates = json_response['coordinates']
            print('room title:', room_title)
            print('room id:', room_id)
            print('coordinates:', coordinates) 
            cool_down = json_response['cooldown']
            time.sleep(cool_down + 1)
           
            # if room_id == 55:
            #     print("wishing well:", room_id)
            #     break

        move = unused_exits[room_id].pop(0)
        direct['direction'] = str(move)
        print('move..............', move)

        old_room_id = room_id
        print('old_room_id...........', old_room_id)
        
        backtrack_path.append(reversed_dir[move])
        move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=direct)
        json_response = move_response.json()
        room_id = json_response['room_id']
        room_exits = json_response['exits']
        room_title = json_response['title']
        coordinates = json_response['coordinates']
        print('room title:', room_title)
        print('room id:', room_id)
        print('coordinates:', coordinates)

        for exit in room_exits: 
            dictionary_entry[exit] = "?"
            world_map[room_id] = dictionary_entry
            world_map[room_id][move] = old_room_id
        print('LELLLLLLLLLLLLLLLLLLLLL', world_map)

        cool_down = json_response['cooldown']
        time.sleep(cool_down + 1)
        
        # if room_id == 55:
        #     print("wishing well:", room_id)
        #     break
    
   

traverseMap()



