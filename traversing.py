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

    world_map[room_id] = {}
    for exit in room_exits: 
        world_map[room_id][exit] = "?"

    print('initial world map', world_map)
    print('cd', cd)
    time.sleep(cd)


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
            print('previous room id', prev_room_id)
            print('MOVING...', previous_dir)
            print('current room id', room_id)
            move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=direct)
            json_response = move_response.json()
            room_id = json_response['room_id']
            room_exits = json_response['exits']
            room_title = json_response['title']
            print('backtracked: room id', room_id)
            print('backtracked: room title', room_title)
            cool_down = json_response['cooldown']
            time.sleep(cool_down)

        move = unused_exits[room_id].pop(0)
        direct['direction'] = str(move)
        backtrack_path.append(reversed_dir[move])
        prev_room_id = room_id
        # print("MOVING...", move)
        move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=direct)
        json_response = move_response.json()
        room_id = json_response['room_id']
        room_title = json_response['title']
        room_exits = json_response['exits']
        # print('new room exits', room_exits)
        print('previous room id', prev_room_id)
        print('MOVING...', move)
        print('current room id', room_id)
        # print('room title', room_title)

        world_map[room_id] = {}
        for exit in room_exits:
            world_map[room_id][exit] = "?"

        world_map[room_id][reversed_dir[move]] = prev_room_id
        world_map[prev_room_id][move] = room_id

        print('new world map', world_map)
        cool_down = json_response['cooldown']
        time.sleep(cool_down)


traverseMap()

"""
TODO:
STORE THE WORLD MAP TO A TEXT FILE

store data somehow someway
    possible solution: save data to a text file 
        then read the saved text file with another searching file thing
        that will spit out shortest route

        run the get init api find our start room
        know our target room
        run the BFS to find the shortest path
        make shortest path into a textfile save it/save it as (start room)-(end room).txt

        when we have shortest path text file, communicate with lambda API
        read path text file to API and call move endpoint for every move

    possible solution2: possibly a database?
"""
