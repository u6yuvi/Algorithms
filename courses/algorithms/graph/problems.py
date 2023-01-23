
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
