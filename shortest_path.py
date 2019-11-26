import ast
from stack_and_queue import Queue

import json

# with open('map.txt') as json_file:
#     data = json.load(json_file)
#     for p in data['1']:
#         print(p)

# with open('map.txt', 'r') as f:
#     s = f.read()
#     print(f"Amount of rooms = {len(ast.literal_eval(s))}")
#     print(s[2])

# def shortest_path(start, destination):
#     q = Queue()
#     q.enqueue([s[start]])
#     visited = set()

#     while q.size() > 0:
#         path = q.dequeue()
#         last_room = path[-1]

#         if last_room not in visited:
#             if last_room == s[destination]:
#                 return path

#             visited.add(last_room)

#             for next_room in s:
#                 path_copy = path.copy()
#                 path_copy.append(next_room)
#                 q.enqueue(path_copy)
 
#     return None

# shortest_path(s[0], s[15])

# def bfs(self, starting_vertex, destination_vertex):
#     """
#     Return a list containing the shortest path from
#     starting_vertex to destination_vertex in
#     breath-first order.
#     """
#     # Create an empty queue and enqueue A PATH to the starting vertex ID
#     q = Queue()
#     q.enqueue([starting_vertex])
#     # Create a Set to store visited vertices
#     visited = set()
#     # While the queue is not empty:
#     while q.size() > 0:
#         #Dequeue the first PATH
#         path = q.dequeue()
#         #grab the last vertex from the PATH
#         v = path[-1]
#         #If that vertex has not been visited...
#         if v not in visited:
#             #Check if it's the target
#             if v == destination_vertex:
#                 #if so, return PATH
#                 return path
#             #Mark it as visited...
#             visited.add(v)
#             #Then add a PATH to its neighbors to the back of the queue
#             # for neighbor in self.get_neighbors(v):
#             for next_v in self.vertices[v]:
#                 #copy the PATH
#                 path_copy = path.copy()
#                 #append the neighbor to the back
#                 path_copy.append(next_v)
#                 q.enqueue(path_copy)
#     #if nothing is found, return None
#     return None