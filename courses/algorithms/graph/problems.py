
import math
#---------------------------Problem-1-------------------------------
'''
343: Count Connected Components In An Undirected Graph
'''
def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """
    '''
    For BFS
    Time Complexity  -  O(n) [ No of nodes] + O(m) 
                        Push/Pop in Queue    + neigbours of each node ~ 
                        
    neigbours of each node - Sum of Degree of each node ~ O(2m)[Undirected] where m is an edge
    
    Space Complexity - Aux Space - O(n) [root node connected to all other nodes]
                        Input Space - O(n+m) [Adj list]
    For DFS
    Time Complexity - O(n)[push/pop in a stack] + O(m)[Looking at adj list of each node as in BFS]
    Sapce Complexity - Aux Space - O(n)

    '''
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
        #    neighbours.append((x+1,y+1))
        # if x+2 <len(matrix) and y+2 <len(matrix[0]):
        #    neighbours.append((x+2,y+2)) 
        # if x-1 >=0 and y-1 >=0:
        #    neighbours.append((x-1,y-1))
        # if x-2 >=0 and y-2 >=0:
        #    neighbours.append((x-2,y-2))
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
[1, 0],
[0, 1]
]
}
# print(count_islands(data["matrix"]))


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


# print(flood_fill(data["pixel_row"],data["pixel_column"],data["new_color"],data["image"]))

#---------------------------Problem-7-------------------------------
def find_town_judge(n, trust):
    """
    Args:
     n(int32)
     trust(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    
    
    # build the tree
    adjlist = [[] for i in range(n)]
    arrival = [-1]*n
    departure = [-1]*n
    visited = [-1]*n
    time = [0]
    #directed graph
    for (src,dst) in trust:
        adjlist[src-1].append(dst-1)
        
    
    #dfs traversal
    def dfs(node):
        arrival[node] = time[0]
        time[0] = time[0] +1
        visited[node] = 1
        for neighbour in adjlist[node]:
            if visited[neighbour]==-1:
                visited[neighbour]=1
                if dfs(neighbour) is True:
                    return True#cycle found
            elif departure[neighbour]==-1:
                return True #cycle found
    
        time[0] = time[0]+1
        departure[node] = time[0]
        return False
    
    #outer loop
    
    for i in range(0,n):
        if visited[i]==-1:
            if dfs(i) is True: # if cyclees found then no judge
                return -1
    
    
    if departure:
        res = departure.index(min(departure))+1
    for i in range(n):
        if i !=res:
            if res not in adjlist[i]:
                return -1
    return res

data = {
"n": 5,
"trust": [
[1, 2],
[3, 2],
[5, 2]
]
}
# print(find_town_judge(data["n"],data["trust"]))


#---------------------------Problem-8-------------------------------
'''
Course Schedule II
'''

'''
If cycles found not possible
Time Complexity - O(m+n)
'''
def course_schedule(n, prerequisites):
    """
    Args:
     n(int32)
     prerequisites(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    
    # build the tree
    adjlist = [[] for i in range(n)]
    arrival = [-1]*n
    departure = [-1]*n
    visited = [-1]*n
    time = [0]
    result_array = []
    #directed graph
    for (src,dst) in prerequisites:
        adjlist[dst].append(src)
        
    
    #dfs traversal
    def dfs(node):
        arrival[node] = time[0]
        time[0] = time[0] +1
        visited[node] = 1
        for neighbour in adjlist[node]:
            if visited[neighbour]==-1:
                visited[neighbour]=1
                if dfs(neighbour) is True:
                    return True#cycle found
            elif departure[neighbour]==-1:
                return True #cycle found
    
        time[0] = time[0]+1
        departure[node] = time[0]
        result_array.append(node)
        return False
    
    #outer loop
    
    for i in range(0,n):
        if visited[i]==-1:
            #dfs(i)
            if dfs(i) is True: # if cyclees found 
                return [-1]
    if result_array:
        return result_array[::-1]
    return [-1]



#---------------------------Problem-9-------------------------------[Few Test Case Failing]
def rotting_oranges(grid):
    """
    Args:
     grid(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    
    
    # traverse
    
    res = [0]
    
    def get_neighbours(x,y):
        result = []
        if x+1 <len(grid):
            if grid[x+1][y] !=0:
                result.append((x+1,y))
        if x-1 >=0:
            if grid[x-1][y]!=0:
                result.append((x-1,y))
                
        if y+1 <len(grid[0]):
            if grid[x][y+1]!=0:
                result.append((x,y+1))
        if y-1 >=0:
            if grid[x][y-1]!=0:
                result.append((x,y-1))
        return result
    
    #traversal
    def bfs():
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
        while q:
            res[0] = res[0]+1
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                for x1,y1 in get_neighbours(node[0],node[1]) :
                    if grid[x1][y1]==1:
                        grid[x1][y1]=2
                        #result[0] = result[0]+1
                        q.append((x1,y1))   
    
    bfs()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                return -1
    
    if res[0]>0:
        return res[0]-1
    return 0
    

data = {
"grid": [
[0]
]
}

# print(rotting_oranges(data["grid"]))

#---------------------------Problem-10-------------------------------[Few Test Case Failing]


def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    """
    Args:
     rows(int32)
     cols(int32)
     start_row(int32)
     start_col(int32)
     end_row(int32)
     end_col(int32)
    Returns:
     int32
    """
    # Write your code here.
    
    #build the graph
    grid = [[-1 for i in range(cols)] for j in range(rows)]
    distance = [0]

    def get_moves(x,y):
        result = []
        [(2,1),(2,-1),[1,2],[-1,2],(-2,1),(-2,-1),(-1,-2),(1,-2)]
        x_grid = [2,2,1,-1,-2,-2,-1,1]
        y_grid = [1,-1,2,2,1,-1,-2,-2]
        for i,j in zip(x_grid,y_grid):
            new_x = i+x
            new_y = j+y
            if 0<= new_x < rows and 0<= new_y<cols:
                result.append((new_x,new_y))
        return result

    def bfs(source):
        q = [source]
        grid[source[0]][source[1]] = distance[0]
        while q:
            distance[0] = distance[0]+1
            cnt = len(q)
            for i in range(cnt):
                node = q.pop(0)
                for x,y in get_moves(node[0],node[1]):
                    if grid[x][y]== -1:
                        grid[x][y]=distance[0]
                        q.append((x,y))
    
    bfs((start_row,start_col))
    
    if grid[end_row][end_col] ==-1:
        return -1
    return grid[end_row][end_col]

# print(find_minimum_number_of_moves(5,5,0,0,4,1))


#---------------------------Problem-10.1-------------------------------[Few Test Case Failing]
'''
Optimised version where shot circuiting once the end row and end column found. No further exploration
'''
def find_minimum_number_of_moves_optimised(rows, cols, start_row, start_col, end_row, end_col):
    """
    Args:
     rows(int32)
     cols(int32)
     start_row(int32)
     start_col(int32)
     end_row(int32)
     end_col(int32)
    Returns:
     int32
    """
    #Shot Circuit to not explore all positions
    #build the graph
    grid = [[-1 for i in range(cols)] for j in range(rows)]
    distance = [0]

    def get_moves(x,y):
        result = []
        [(2,1),(2,-1),[1,2],[-1,2],(-2,1),(-2,-1),(-1,-2),(1,-2)]
        x_grid = [2,2,1,-1,-2,-2,-1,1]
        y_grid = [1,-1,2,2,1,-1,-2,-2]
        for i,j in zip(x_grid,y_grid):
            new_x = i+x
            new_y = j+y
            if 0<= new_x < rows and 0<= new_y<cols:
                result.append((new_x,new_y))
        return result

    def bfs(source):
        q = [source]
        grid[source[0]][source[1]] = distance[0]
        while q:
            distance[0] = distance[0]+1
            cnt = len(q)
            for i in range(cnt):
                node = q.pop(0)
                for x,y in get_moves(node[0],node[1]):
                    if grid[x][y]== -1:
                        grid[x][y]=distance[0]
                        if x==end_row and y == end_col:
                            return grid[end_row][end_col]
                        q.append((x,y))
        return grid[end_row][end_col]
    
    # bfs((start_row,start_col))
    
    # if grid[end_row][end_col] ==-1:
    #     return -1
    # return grid[end_row][end_col]

    res = bfs((start_row,start_col))
    if res!=-1:
        return res
    return -1
    
# print(find_minimum_number_of_moves_optimised(1,1,0,0,0,0))




def get_all_shortest_transformation_sequences(start_word, target_word, words):
    """
    Args:
     start_word(str)
     target_word(str)
     words(list_str)
    Returns:
     list_list_str
    """
    # Write your code here.
    visited = [-1]*len(words)
    result = [0]
    path = []
    wrd2idx = {wrd:idx for idx,wrd in enumerate(words)}
    parent = [-1]*len(words)
    parents = []

    def get_neighbours(text):
        result = []
        for wrd in words:
            diff_sum = [ 1 for t_char,wrd_char in zip(text,wrd) if t_char !=wrd_char ]
            if sum(diff_sum)==1:
                result.append(wrd)
        return result

    def bfs(source):
        q = [source]
        path.append(source)
        #visited[wrd2idx[source]]=1
        while q:
           
            parent = [-1]*len(words)
            cnt = len(q)
            result[0] = result[0] +1
            for i in range(cnt):
                node = q.pop(0)
                for neighbour in get_neighbours(node):
                    if visited[wrd2idx[neighbour]]==-1:
                        parent[wrd2idx[neighbour]] = node
                        visited[wrd2idx[neighbour]]= 1
                        if neighbour == target_word:
                            parents.append(parent)
                            return True
                        q.append(neighbour)
            parents.append(parent)
        return False

    res = bfs(start_word)

        #print(result)
            
data = {
"start_word": "hot",
"target_word": "dog",
"words": ["cat", "dog", "hat", "dot", "cot", "hog"]
}
# print(get_all_shortest_transformation_sequences(data["start_word"],data["target_word"],data["words"]))



# def alien_text(words):

#     {"b":[]}

'''
1129. Shortest Path with Alternating Colors
'''
def shortestAlternatingPaths( n: int, redEdges, blueEdges):
        

    #create adjacency list
    adjlist = [[] for _ in range(n)]
    for src,dst in redEdges:
        adjlist[src].append((dst,0))
    
    for src, dst in blueEdges:
        adjlist[src].append((dst,1))

    visited = [()]*n
    dist = [float("inf")]*n
    def bfs():
        level = 0
        q = [(0,0),(0,1)]
        #visited[node[0]] = 1
        
        while q:
            for _ in range(len(q)):
                node, color = q.pop(0)
                dist[node] = min(dist[node],level)
                for neig,neig_color in adjlist[node]:
                    if color !=neig_color and (neig,neig_color) not in visited:
                        q.append((neig,neig_color))
                        visited.append((neig,neig_color))
            level = level+1
        
        return dist



    bfs()
    return [i if i!=float('inf') else -1 for i in dist]

red = [[0,1]]
blue = [[2,1]]
# print(shortestAlternatingPaths(3,red,blue))



def maxDistance(grid):
        
    def get_neigh(i,j):
        result = []
        if i+1 <len(grid): 
            if grid[i+1][j]!=1:
                result.append((i-1,j-1))
        if i-1 >=0:
            if grid[i-1][j]!=1:
                result.append((i-1,j))
        if j-1 >=0:
            if grid[i][j-1]!=1:
                result.append((i,j-1))
                
        if j+1 < len(grid[0]):
            if grid[i][j+1]!=1:
                result.append((i,j+1))
        return result
                        

    def bfs():
        q = []
        #get all 1's in the queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    q.append((i,j))
        #start bfs
        dist = 0
        while q:
            for i in range(len(q)):
                node = q.pop(0)
                for x,y in get_neigh(node[0],node[1]):
                    if grid[x][y]!=1:
                        grid[x][y]=1
                        q.append((x,y))
            dist = dist +1
        return dist

    dist = bfs()
    if dist==0 or dist==1:
        return -1
    return dist-1


grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

# print(maxDistance(grid))

def minimumFuelCost( roads, seats) -> int:
        
    if not roads:
        return 0 
    adjlist = [[] for i in range(len(roads)+1)]
    visited = [-1]*(len(roads)+1)
    parent = [-1]*(len(roads)+1)
    for src,dst in roads:
        adjlist[src].append(dst)
        adjlist[dst].append(src)
    
    # level = [0]
    # fuel = [0]
    # def bfs():
    #     # for i in adjlist:
    #     #     if 
    #     q = adjlist[0]
    #     for idx,i in enumerate(adjlist):
    #         if 0 in i:
    #             q.append(adjlist[idx])
    #     while q:
    #         cnt = len(q)
    #         node = q.pop(0)
    #         for _ in range(cnt):
    #             node = q.pop(0)
    #             for neigh in adjlist[node]:
    #                 if visited[neigh]==-1:
    #                     visited[neigh] ==1
    #                     q.append(neigh)
            
    #         seat = seats-1
    #         level[0] = level[0]+1
    #         if seat>=0:
    #             fuel[0] = fuel[0]+ len(q)
            
    #         if seat<0:
    #             seat=seats
    #             fuel[0] = fuel[0] + level[0]*len(q)
                
    #     return fuel
    
    fuel = [0]
    def dfs(node):
        repr1 = 1
        result = []
        visited[node]=1   

        for neigh in adjlist[node]:
            if visited[neigh]==-1:
                visited[neigh]==1
                #parent[neigh] = node
                res = dfs
                res%2
                result.append(dfs(neigh))
        #if node!=0:
            #repr = repr +1
            #fuel[0] = fuel[0] + math.ceil((repr1)/seats)
        if node!=0:
            repr1 = sum(result)+1
            fuel[0] = fuel[0] + math.ceil((repr1)/seats)
        return repr1


    
    res = dfs(0)
    return fuel[0]



roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
seats = 2
print(minimumFuelCost(roads,seats))