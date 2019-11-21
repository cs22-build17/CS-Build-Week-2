import requests
import time
def traverseMap():
    headers = {
        'Authorization': f"Token 2fc47453e51b1846650157a33637a2dae7c8575f",
        'Content-Type': 'application/json',
    }
    # world_map = {}
    unused_exits = {}
    backtrack_path = []
    reversed_dir = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
    direct = {}
    # world_map = {}
    init_response = requests.get(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers)
    init_data = init_response.json()
    room_title = init_data['title']
    room_id = init_data['room_id']
#    coordinates = init_data['coordinates']
    print('initial room id', room_id)
    cd = init_data['cooldown']
    room_exits = init_data['exits']
    unused_exits[room_id] = room_exits
    # world_map[room_id][0] = room_title
    # world_map[room_id][1] = coordinates
    print(init_data)
    print('cd', cd)
    time.sleep(cd + 1)
#    print(world_map)
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
            move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=direct)
            json_response = move_response.json()
            room_id = json_response['room_id']
            room_exits = json_response['exits']
            room_title = json_response['title']
            print('room id', room_id)
            print('room title', room_title)
            cool_down = json_response['cooldown']
            time.sleep(cool_down + 1)
             if room_title == "Pirate Ry's":
                 print("pirate rys is:", room_id)
                 break
        move = unused_exits[room_id].pop(0)
        direct['direction'] = str(move)
        backtrack_path.append(reversed_dir[move])
        move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=direct)
        json_response = move_response.json()
        room_id = json_response['room_id']
        room_title = json_response['title']
        room_exits = json_response['exits']
        print('room id', room_id)
        print('room title', room_title)
        cool_down = json_response['cooldown']
        time.sleep(cool_down + 1)
         if room_title == "Pirate Ry's":
             print("pirate rys is:", room_id)
             break
traverseMap()