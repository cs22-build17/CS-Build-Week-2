import requests
import time

def traverseMap():
    headers = {
        'Authorization': f"Token 590ad42a7fa794202fb1f779d78cd5739ae256a1",
        'Content-Type': 'application/json',
    }

    traversalPath = []
    world_map = {}
    visited = {}
    path = []
    reversed_dir = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

    init_response = requests.get(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers)
    init_data = init_response.json()
    # current_room = init_data['title']
    room_id = init_data['room_id']
    cd = init_data['cooldown']
    coordinates = init_data['coordinates']
    room_exits = init_data['exits']
    # print(room_exits)
    # print(init_data)
    visited[room_id] = room_exits
    world_map[room_id] = room_exits
    print('cd', cd)
    time.sleep(cd + 1)

    # direct = {'direction':'s'}
    direct = {}

    # move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=direct)
    # json_response = move_response.json()
    # cool_down = json_response['cooldown']

    while len(visited) < 499:
        if room_id not in visited:
            print('id', room_id)
            visited[room_id] = room_exits
            world_map[room_id] = room_exits
            previous_dir = path[-1]

            visited[room_id].remove(previous_dir)
            print('visited', visited)

        while len(visited[room_id]) == 0:
            # print('path', path)
            previous_dir = path.pop()
            # print('previous', previous_dir)
            traversalPath.append(previous_dir)
            direct['direction'] = str(previous_dir)
            move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=direct)
            json_response = move_response.json()
            # print('inside', json_response)
            cool_down = json_response['cooldown']
            time.sleep(cool_down + 1)

        move = visited[room_id].pop(0)
        direct['direction'] = str(move)
        traversalPath.append(move)
        path.append(reversed_dir[move])
        # print('move', move)
        # print('path', path)
        move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=direct)
        json_response = move_response.json()
        # print('outside', json_response)
        cool_down = json_response['cooldown']
        time.sleep(cool_down + 1)
        # print('world', world_map)

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