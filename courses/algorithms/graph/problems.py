

#---------------------------Problem-1-------------------------------
'''
Count Connected Components In An Undirected Graph
'''
def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    
    #build graph
    adjlist = [[] for _ in range(0,n)]
    visited = [-1]*n
    for (src,dst) in edges:
        adjlist[src].append(dst)
        adjlist[dst].append(src)
        
    
    #bfs
    
    def bfs(source):
        q = [source]
        visited[source] = 1 
        while q:
            node = q.pop(0)
            for neighbour in adjlist[node]:
                if visited[neighbour]==-1:
                    visited[neighbour] = 1
                    q.append(neighbour)
    
    
    
    #outer loop
    component = 0
    for node in range(0,n):
        if visited[node]==-1:
            component = component+1
            bfs(node)
            
    return component







#---------------------------Problem-2-------------------------------
'''
Given an undirected graph, find out whether it is a tree.
'''
def is_it_a_tree(node_count, edge_start, edge_end):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    

    #Build Graph
    parent = [-1]*node_count
    visited = [-1]*node_count
    adjlist = [[] for i in range(0,node_count)]
    
    for (src,dst) in zip(edge_start,edge_end):
        adjlist[src].append(dst)
        adjlist[dst].append(src)
    
        
    #bfs
    
    # def bfs(source):
    #     q = [source]
    #     visited[source] = 1
    #     while q:
    #         node = q.pop(0)
    #         for neighbour in adjlist[node]:
    #             if visited[neighbour]==-1:
    #                 visited[neighbour] =1
    #                 parent[neighbour] = node
    #                 q.append(neighbour)
    #             else: # check for cross edge
    #                 if neighbour !=parent[node]:
    #                     return True # is cyclic
    #     return False
                   
    #dfs
    def dfs(node):
        visited[node] = 1
        for neighbour in adjlist[node]:
            if visited[neighbour]==-1:
                parent[neighbour] = node
                if dfs(neighbour) is True:
                    return True 
            elif neighbour !=parent[node]:
                return True #inner stack returning the value
        return False
            
    
    # Outer loop
    components = 0
    for n_i in range(0,node_count):
        if visited[n_i]==-1:
            components =components +1
            if components >1:
                return False # is not connected
            
            if dfs(n_i) is True: # check if cyclic
                return False  #final decision - not a tree
    
    
    return True

data = {
"node_count": 4,
"edge_start": [0, 0, 0],
"edge_end": [1, 2, 3]
}
# print(is_it_a_tree(data["node_count"],data["edge_start"],data["edge_end"]))



#---------------------------Problem-2-------------------------------
'''
Is Graph Bipartite
'''

def can_be_divided(num_of_people, dislike1, dislike2):
    """
    Args:
     num_of_people(int32)
     dislike1(list_int32)
     dislike2(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    
    
    #Build the graph
    adjlist = [[] for i in range(num_of_people)]
    visited = [-1]*num_of_people
    parent = [-1]*num_of_people
    distance = [-1]*num_of_people
    for src,dst in zip(dislike1,dislike2):
        adjlist[src].append(dst)
        adjlist[dst].append(src)
        
    
    
    #BFS
    
    def bfs(source):
        q = [source]
        visited[source] = 1
        while q:
            node = q.pop(0)
            for neighbour in adjlist[node]:
                if visited[neighbour]==-1:
                    visited[neighbour] = 1
                    parent[neighbour] = node
                    distance[neighbour] = distance[node] + 1
                    q.append(neighbour)
                else:
                    if parent[node] != neighbour:
                        if distance[neighbour] ==distance[node]:
                            return False#not bipartite
        return True
    
    
    #Outer loop
    for i in range(0,num_of_people):
        if visited[i]==-1:
            if bfs(i) is False:
                return False
    return True


#---------------------------Problem-3-------------------------------
def can_be_completed(n, a, b):
    """
    Args:
     n(int32)
     a(list_int32)
     b(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    
    #build the graph
    adjlist = [[] for i in range(n)]
    visited = [-1]*n
    arrival = [-1]*n
    departure = [-1]*n
    timestamp = [0]
    #directed graph
    for (src,dst) in zip(a,b):
        adjlist[dst].append(src)
    
    #dfs with rrival departure recording
    def dfs(node):
        arrival[node] = timestamp[0] 
        timestamp[0] = timestamp[0] +1
        visited[node]=1
        for neighbour in adjlist[node]:
            if visited[neighbour]==-1:
                if dfs(neighbour) is True:
                    return True #cycle found so course not possible
            elif departure[neighbour]==-1:
                    return True
        departure[node] = timestamp[0]
        timestamp[0] = timestamp[0]+1
        
        return False
        
    #outer loop
    for i in range(0,n):
        if visited[i]==-1:
            if dfs(i) is True:
                return False
    
    
    return True






data = {
"n": 4,
"a": [1, 1, 3, 0],
"b": [0, 2, 1, 3]
}
print(can_be_completed(data["n"],data["a"],data["b"]))
'''
{
"n": 3,
"a": [0, 1, 2],
"b": [1, 2, 0]
}
'''

#---------------------------Problem-4-------------------------------[TODO]

'''
Count Islands
'''


def count_islands(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    
            
    def get_neighbors(x,y):
        neighbours = []
        if x+1 < len(matrix):
            neighbours.append((x+1,y))
        if x+2 < len(matrix):
            neighbours.append((x+2,y))
        if x-1 >=0 :
            neighbours.append((x-1,y))
        if x-2 >= 0:
            neighbours.append((x-2,y))
        
        
        #vertical neighbours
        if y+1 < len(matrix[0]):
            neighbours.append((x,y+1))
        if y+2 < len(matrix[0]):
            neighbours.append((x,y+2))
        if y-1 >=0 :
            neighbours.append((x,y-1))
        if y-2 >= 0:
            neighbours.append((x,y-2))
        #diagonal
        if x+1 <len(matrix) and y+1 <len(matrix[0]):
           neighbours.append((x+1,y+1))
        if x+2 <len(matrix) and y+2 <len(matrix[0]):
           neighbours.append((x+2,y+2)) 
        if x-1 >=0 and y-1 >=0:
           neighbours.append((x-1,y-1))
        if x-2 >=0 and y-2 >=0:
           neighbours.append((x-2,y-2))
        return neighbours
    
    #bfs traversal
    def bfs(source):
        q = [source]
        matrix[source[0]][source[1]] = 0
        while q:
            x,y = q.pop(0)
            for neighbors in get_neighbors(x,y):
                if matrix[neighbors[0]][neighbors[1]] !=0:
                    matrix[neighbors[0]][neighbors[1]] = 0
                    q.append(neighbors)
                    
                    
                    
                    
    #outer loop
    components = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] !=0:
                bfs((i,j))
                components = components +1
    
    return components


data = {
"matrix": [
[1],
[1],
[1],
[0],
[1],
[1],
[1],
[1]
]
}
print(count_islands(data["matrix"]))


#---------------------------Problem-5-------------------------------

'''
Find Largest Island
'''

def max_island_size(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    distance = [0]
            
    def get_neighbors(x,y):
        neighbours = []
        if x+1 < len(matrix):
            neighbours.append((x+1,y))
        # if x+2 < len(matrix):
        #     neighbours.append((x+2,y))
        if x-1 >=0 :
            neighbours.append((x-1,y))
        # if x-2 >= 0:
        #     neighbours.append((x-2,y))
        
        
        #vertical neighbours
        if y+1 < len(matrix[0]):
            neighbours.append((x,y+1))
        # if y+2 < len(matrix[0]):
        #     neighbours.append((x,y+2))
        if y-1 >=0 :
            neighbours.append((x,y-1))
        # if y-2 >= 0:
        #     neighbours.append((x,y-2))
        #diagonal
        # if x+1 <len(matrix) and y+1 <len(matrix[0]):
        #   neighbours.append((x+1,y+1))
        # if x+2 <len(matrix) and y+2 <len(matrix[0]):
        #   neighbours.append((x+2,y+2)) 
        # if x-1 >=0 and y-1 >=0:
        #   neighbours.append((x-1,y-1))
        # if x-2 >=0 and y-2 >=0:
        #   neighbours.append((x-2,y-2))
        return neighbours
    
    #bfs traversal
    def bfs(source):
        q = [source]
        matrix[source[0]][source[1]] = 0
        distance[0] = distance[0]+1
        while q:
            x,y = q.pop(0)
            for neighbors in get_neighbors(x,y):
                if matrix[neighbors[0]][neighbors[1]] !=0:
                    matrix[neighbors[0]][neighbors[1]] = 0
                    distance[0] = distance[0]+1
                    q.append(neighbors)
                    
                    
                    
                    
    #outer loop
    dist = []
    components = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] !=0:
                bfs((i,j))
                components = components +1
                dist.append(distance[0])
                distance = [0]
    
    if dist:
        return max(dist)
    return 0


#---------------------------Problem-6-------------------------------

def flood_fill(pixel_row, pixel_column, new_color, image):
    """
    Args:
     pixel_row(int32)
     pixel_column(int32)
     new_color(int32)
     image(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    
    pixl_color = [image[pixel_row][pixel_column]]
    
    def get_neighbors(x,y):
        result = []
        if x+1 < len(image):
            result.append((x+1,y))
        if x-1 >=0 :
            result.append((x-1,y))
        if y+1<len(image[0]):
            result.append((x,y+1))
        if y-1 >=0:
            result.append((x,y-1))
        return result
    #bfs
    
    def bfs(x,y):
        q = [(x,y)]
        image[x][y] = new_color
        while q:
            x1,y1 = q.pop(0)
            for i,j in get_neighbors(x1,y1):
                if image[i][j] == pixl_color[0]:
                    image[i][j] = new_color
                    q.append((i,j))
    
    #outer loop
    
    if image[pixel_row][pixel_column] != new_color:
        bfs(pixel_row,pixel_column)
    
    return image


data = {
"pixel_row": 0,
"pixel_column": 1,
"new_color": 2,
"image": [
[0, 1, 3],
[1, 1, 1],
[1, 5, 4]
]
}

flood_fill