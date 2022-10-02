# #   Created by Elshad Karimov 
# #   Copyright © 2021 AppMillers. All rights reserved.

# from threading import get_ident
# from tkinter import N


# class Graph:
#     def __init__(self, gdict=None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict
    
#     def addEdge(self, vertex, edge):
#         self.gdict[vertex].append(edge)
    
#     def bfs(self, vertex):
#         visited = [vertex]
#         queue = [vertex]
#         while queue:
#             deVertex = queue.pop(0)
#             print(deVertex)
#             for adjacentVertex in self.gdict[deVertex]:
#                 if adjacentVertex not in visited:
#                     visited.append(adjacentVertex)
#                     queue.append(adjacentVertex)
    
#     def dfs(self, vertex):
#         visited = [vertex]
#         stack = [vertex]
#         while stack:
#             popVertex = stack.pop()
#             print(popVertex)
#             for adjacentVertex in self.gdict[popVertex]:
#                 if adjacentVertex not in visited:
#                     visited.append(adjacentVertex)
#                     stack.append(adjacentVertex)
    



# customDict = { "a" : ["b","c"],
#             "b" : ["a", "d", "e"],
#             "c" : ["a", "e"],
#             "d" : ["b", "e", "f"],
#             "e" : ["d", "f", "c"],
#             "f" : ["d", "e"]
#                }



# g = Graph(customDict)
# g.dfs("a")





class Graph:
    def __init__(self,gdict):
        if gdict is None:
            self.gdict = {}
        self.gdict = gdict

    def add_edge(self,vertex,edge):
        if vertex in self.gdict:
            self.gdict[vertex].append(edge)

    
    def bfs(self,vertex):
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
            for adjvetex in self.gdict[deVertex]:
                if adjvetex not in visited:
                    visited.append(adjvetex)
                    queue.append(adjvetex)

    def dfs(self,vertex):
        '''
        push any starting vertex
        make it visited
        while stack is not empty
            p = pop()
            push all adjacent unvisited vertices of p
            '''
        visited = [vertex] #make it visited
        stack = [vertex] # push the element

        while stack: 
            deVertex = stack.pop()
            print(deVertex)
            for adjvertex in self.gdict[deVertex]:
                if adjvertex not in visited:
                    visited.append(adjvertex) # mark all adjacent vertex visited
                    stack.append(adjvertex) # push all adjacent vertex in stack

customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }
g = Graph(customDict)
g.dfs("a")
    


