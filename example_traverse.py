import requests
from stack_and_queue import Stack 
import time 


def traverseMap():

    headers = {
        'Authorization': f"Token 7922ffc0cc5d060b72e31aa06131cddc3b7775f7",
        'Content-Type': 'application/json',
    }

    init_response = requests.get(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers)
    init_data = init_response.json()

    room_id = init_data['room_id']
    current_room = init_data['title']
    description = init_data['description']
    coordinates = init_data['coordinates']
    exits = init_data['exits']
    print(f"Here is the room we're currently in..... {room_id}")

    move_yo = {"direction": "s"}
    # {"direction":"s", "next_room_id": "0"}
    move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=move_yo)
    # move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', {"direction": "s"})
    # move_response = requests.post(url=move, headers={"Authorization": token}, json={'name': f'{move}'})
    print(f"this is our move response..... {move_response}")

    # time.sleep(init_data['cooldown'])
    # cool = init_data['cooldown']
    # print(cool)

    visited = {}

    visited[room_id] = exits

    # print(visited)

    path = []
    reversed_dir = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
    traversalPath = []


    # while len(visited) < 500:

    #     if room_id not in visited:
    #         visited[room_id] = exits
    #         previous_dir = path[-1]
    #         visited[room_id].remove(previous_dir)

    #     while len(visited[room_id]) == 0:
    #         previous_dir = path.pop()
    #         traversalPath.append(previous_dir)
    #         # player.travel(previous_dir)
    #         # {"direction":"s", "next_room_id": "0"}
            
    #         move_yo = {'direction': previous_dir}
    #         move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=move_yo)
    #         print(f"this is our move response..... {move_response}")
        
    #     move = visited[room_id].pop(0)

    #     traversalPath.append(move)

    #     path.append(reversed_dir[move])

        # player.travel(move)



traverseMap()





# hello = {
#   "room_id": 0,
#   "title": "A Brightly Lit Room",
#   "description": "You cannot see anything.",
#   "coordinates": "(60,60)",
#   "exits": ["n", "s", "e", "w"],
#   "cooldown": 1.0,
#   "errors": [],
#   "messages": []
# }


# print(hello)