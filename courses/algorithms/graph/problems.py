

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
print(is_it_a_tree(data["node_count"],data["edge_start"],data["edge_end"]))



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