import requests
import time

def traverseMap():
    headers = {
        'Authorization': f"Token 590ad42a7fa794202fb1f779d78cd5739ae256a1",
        'Content-Type': 'application/json',
    }

    world_map = {}
    unused_exits = {}
    backtrack_path = []
    reversed_dir = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
    direct = {}
    new_dict_entry = {}
    prev_dict_entry = {}

    init_response = requests.get(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers)
    init_data = init_response.json()
    # print(init_data)
    # room_title = init_data['title']
    room_id = init_data['room_id']
    # coordinates = init_data['coordinates']
    print('initial room id', room_id)
    cd = init_data['cooldown']
    room_exits = init_data['exits']
    unused_exits[room_id] = room_exits
    for exit in room_exits: 
        new_dict_entry[exit] = "?"
        print('init new dict', new_dict_entry)
        world_map[room_id] = new_dict_entry
    print('init map', world_map)
    new_dict_entry.clear()
    print('cleared', new_dict_entry)
    # print(init_data)
    print('cd', cd)
    time.sleep(cd)
    # print(world_map)

#DEBUGGING BLOCK BELOW
    # direct = {'direction':'s'}
    # print(unused_exits)
    # move = unused_exits[room_id].pop(0)
    # direct['direction'] = str(move)
    # print('move', move)
    # move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=direct)
    # json_response = move_response.json()
    # room_id = json_response['room_id']
    # cool_down = json_response['cooldown']
    # print('new room id', room_id)
    # time.sleep(cool_down + 1)

    while len(unused_exits) < 499:
        if room_id not in unused_exits:
            unused_exits[room_id] = room_exits
            previous_dir = backtrack_path[-1]
            unused_exits[room_id].remove(previous_dir)

        while len(unused_exits[room_id]) == 0:
            previous_dir = backtrack_path.pop()
            direct['direction'] = str(previous_dir)
            prev_room_id = room_id
            print('previous room id:', prev_room_id)
            print("MOVING...", previous_dir)
            move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=direct)
            json_response = move_response.json()
            room_id = json_response['room_id']
            room_exits = json_response['exits']
            room_title = json_response['title']
            print('new room id', room_id)
            # print('room title', room_title)
            cool_down = json_response['cooldown']
            time.sleep(cool_down)
            # if room_title == "Pirate Ry's":
            #     print("pirate rys is:", room_id)
            #     break

        move = unused_exits[room_id].pop(0)
        direct['direction'] = str(move)
        backtrack_path.append(reversed_dir[move])
        prev_room_id = room_id
        print("MOVING...", move)
        move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=direct)
        json_response = move_response.json()
        room_id = json_response['room_id']
        room_title = json_response['title']
        room_exits = json_response['exits']
        print('new room id', room_id)
        print('room title', room_title)
        print('prev room id', prev_room_id)
        # print(str(move))
        # world_map[prev_room_id][str(move)] = room_id
        for room in world_map:
            if room == room_id:
                for exit in room_exits: 
                    # if new_dict_entry[exit] is None:
                    new_dict_entry[exit] = "?"
                    print('new dict entry', new_dict_entry)
                    # world_map[room_id] = new_dict_entry
                    print('loop world map', world_map)
        new_dict_entry[reversed_dir[move]] = prev_room_id
        print('reversed move dict', new_dict_entry)
        world_map[room_id] = new_dict_entry
        # print('after loop map', world_map)
        # new_dict_entry.clear()
        print('cleared2', new_dict_entry)
        new_dict_entry[move] = room_id
        world_map[prev_room_id] = new_dict_entry
        # new_dict_entry.clear()
        print('last map', world_map)
        # prev_dict_entry[move] = room_id
        # world_map[prev_room_id][move] = old_room_id
        # print('new world map:', world_map)
        cool_down = json_response['cooldown']
        time.sleep(cool_down)
        # if room_title == "Pirate Ry's":
        #     print("pirate rys is:", room_id)
        #     break

traverseMap()

# token = "Token "

# api-endpoint
# init        = "https://lambda-treasure-hunt.herokuapp.com/api/adv/init/"
# move        = "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/"
# take        = "https://lambda-treasure-hunt.herokuapp.com/api/adv/take/"
# changeName  = "https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/"
# sale        = "https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/"
# examineItem = "https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/"

#####TODO#####
#json object that contains room information

#inplement graph traversal and building

#account visited room path

#reverse direction incase needs to go back.

#account cooldown time.

#request to the server
##############

