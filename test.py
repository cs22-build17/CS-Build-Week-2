import requests
import time

def traverseMap():
    headers = {
        'Authorization': f"Token 590ad42a7fa794202fb1f779d78cd5739ae256a1",
        'Content-Type': 'application/json',
    }
    # init_response = requests.get(
    #     'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers)
    # init_data = init_response.json()
    # current_room = init_data['title']
    # room_id = init_data['room_id']
    # cd = init_data['cooldown']
    # coordinates = init_data['coordinates']
    # room_exits = init_data['exits']
    # print(f"Room ID:{room_id}, Exits:{room_exits}, Coordinates:{coordinates}, Cool Down:{cd}")

    move = {"direction":"n"}
    move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=move)
    json_response = move_response.json()
    room_id = json_response['room_id']
    title = json_response['title']
    description = json_response['description']
    exits = json_response['exits']
    cool_down = json_response['cooldown']

    # move_data = move_response.json()
    # print(f"this is our move response... {move_response}")
    print(move_response)
    print(json_response)
    print(room_id)
    print(exits)
    print(cool_down)
    # print(content_data)

    # traversalPath = []
    # world_map = {}
    # visited = {}
    # path = []
    # reversed_dir = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

    # init_response = requests.get(
    #     'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers)
    # init_data = init_response.json()
    # current_room = init_data['title']
    # room_id = init_data['room_id']
    # cd = init_data['cooldown']
    # coordinates = init_data['coordinates']
    # room_exits = init_data['exits']

    # visited[room_id] = exits
    # world_map[room_id] = exits

    # while len(visited) < 499:
    #     if room_id not in visited:
    #         visited[room_id] = exits
    #         world_map[room_id] = exits
    #         previous_dir = path[-1]

    #         visited[room_id].remove(previous_dir)

    #     while len(visited[room_id]) == 0:
    #         previous_dir = path.pop()
    #         traversalPath.append(previous_dir)
    #         move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=previous_dir)
    #         cool_down = json_response['cooldown']
    #         time.sleep()

    #     move = visited[room_id].pop(0)
    #     traversalPath.append(move)
    #     path.append(reversed_dir[move])
    #     player.travel(move)

traverseMap()