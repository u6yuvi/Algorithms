# #   Created by Elshad Karimov 
# #   Copyright © 2021 AppMillers. All rights reserved.

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def bfs(self, vertex):
        '''
        1. Enque any starting vertex.
        2. While queue is not empty
            p = dequeue
            if p is unvisited:
                make p visited 
                enqueue all the adjacent unvisited vertices of p
        '''
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
    
    def dfs(self, vertex):
        '''
        push any starting vertex
        make it visited
        while stack is not empty
            p = pop()
            push all adjacent unvisited vertices of p
            '''
        visited = [vertex] #make it visited
        stack = [vertex] #push the element
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex) # mark all adjacent vertex visited
                    stack.append(adjacentVertex) # push all adjacent vertex in stack
    



customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }



g = Graph(customDict)
g.dfs("a")



