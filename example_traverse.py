# import requests
# from stack_and_queue import Stack 
# import time 


# def traverseMap():
    
#     headers = {
#         'Authorization': f"Token 7922ffc0cc5d060b72e31aa06131cddc3b7775f7",
#         'Content-Type': 'application/json',
#     }
    
#     init_response = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers)
#     init_data = init_response.json()
#     time.sleep(2)
#     current_room_title = init_data['title']
#     room_id = init_data['room_id']
#     cd = init_data['cooldown']
#     coordinates = init_data['coordinates']
#     room_exits = init_data['exits']
#     print(f"Room ID:{room_id}, Exits:{room_exits}, Coordinates:{coordinates}, Cool Down:{cd}")
   
#     move = {"direction":"n"}
#     move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=move)
#     print(f"this is our move repsonse...... {move_response}")

#     json_response = move_response.json()

#     print(f"this is our JSON move repsonse...... {json_response}")
    
#     cool_down = json_response['cooldown']
#     print(f"this is our cool down........ {cool_down}")
    
    
#     # map = {
#     #         0: { 'n': '?', 's': 2, 'e': 4, 'w': 1, 'title': current_room_title},
#     #         2: { 'n': 0, 's': None, 'e': 3, 'w': None, 'title': "A misty room"},
#     #         3: { 'n': None, 's': 9, 'e': 5, 'w': 2, 'title': "Mt. Holloway"},
#     #         4: { 'n': 23, 's': None, 'e': 13, 'w': 0, 'title': "A misty room"}
#     #     }
    


#     world_map = {}

#     world_map[room_id] = room_exits

#     print(f"this is our exits: {world_map}")

#     visited = {}

#     visited[room_id] = room_exits


#     path = []
#     reversed_dir = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
#     traversalPath = []

#     while len(visited) < 499:
#         if room_id not in visited:
#             visited[room_id] = room_exits
#             world_map[room_id] = room_exits
#             previous_dir = path[-1]
#             visited[room_id].remove(previous_dir)

#         while len(visited[room_id]) == 0:
#             previous_dir = path.pop()
#             print(f"this is our previous direction... {previous_dir}")
#             traversalPath.append(previous_dir)
#             move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=previous_dir)
#             json_response = move_response.json()    
#             cool_down = json_response['cooldown']
#             time.sleep(cool_down + 1)

#         move = visited[room_id].pop(0)
#         traversalPath.append(move)
#         path.append(reversed_dir[move])
#         move_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, json=previous_dir)
#         json_response = move_response.json()   
#         cool_down = json_response['cooldown']
#         time.sleep(cool_down + 1)

# traverseMap()