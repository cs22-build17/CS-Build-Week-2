import ast

# def reading(self):
#     with open('deed.txt', 'r') as f:
#         s = f.read()
#         self.whip = ast.literal_eval(s)



def read_data():
    with open('map.txt', 'r') as f:
        s = f.read()
        print(len(ast.literal_eval(s)))


read_data()

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH to the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty:
        while q.size() > 0:
            #Dequeue the first PATH
            path = q.dequeue()
            #grab the last vertex from the PATH
            v = path[-1]
            #If that vertex has not been visited...
            if v not in visited:
                #Check if it's the target
                if v == destination_vertex:
                    #if so, return PATH
                    return path
                #Mark it as visited...
                visited.add(v)
                #Then add a PATH to its neighbors to the back of the queue
                # for neighbor in self.get_neighbors(v):
                for next_v in self.vertices[v]:
                    #copy the PATH
                    path_copy = path.copy()
                    #append the neighbor to the back
                    path_copy.append(next_v)
                    q.enqueue(path_copy)
        #if nothing is found, return None
        return None