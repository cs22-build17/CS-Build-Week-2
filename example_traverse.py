import requests
from stack_and_queue import Stack 
import time 


def traverseMap():
    
    headers = {
        'Authorization': f"Token 2fc47453e51b1846650157a33637a2dae7c8575f",
        'Content-Type': 'application/json',
    }
    
    init_response = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers)
    init_data = init_response.json()
    time.sleep(2)
    current_room = init_data['title']
    room_id = init_data['room_id']
    cd = init_data['cooldown']
    coordinates = init_data['coordinates']
    room_exits = init_data['exits']
    print(f"Room ID:{room_id}, Exits:{room_exits}, Coordinates:{coordinates}, Cool Down:{cd}")
    move = {"direction":"n"}
    move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=move)
    time.sleep(16)
    # json_response = move_response.json()
    # move_data = json_response['data']
    # content_data = json_response['headers']['Content-Type']
    # move_data = move_response.json()
    # print(f"this is our move response... {move_response}")
    print(move_response)
    # print(move_data)
    # print(content_data)
    init_response = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers)
    init_data = init_response.json()
    time.sleep(2)
    room_id2 = init_data['room_id']
    print(f"Room ID:{room_id2}")    
    #visited = {}

    #visited[room_id] = exits

    # print(visited)

    #path = []
    #reversed_dir = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
    #traversalPath = []


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