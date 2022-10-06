# create a graph

from collections import deque
class Graph:
    def __init__(self,gdict = None):
        self.gdict = gdict



    def bfs(self,vertex):
        '''
        Enqueue any starting vertex
        While queue is not empty
            p = dequeue()
            if p not visited:
                make p visited
                enqueue all adjacent unvisited vertices of p
            
        Time Complexity - O(V+E)
        space Complexitiy - O(V+E)


        '''
        visited = [vertex]
        queue = [vertex]
        while queue:
            q = queue.pop(0)
            print(q)
            for ajdvertec in self.gdict[q]:
                if ajdvertec not in visited:
                    visited.append(ajdvertec)
                    queue.append(ajdvertec)



    def dfs(self,vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            s = stack.pop()
            print(s)
            for adjv in self.gdict[s]:
                if adjv not in visited:
                    visited.append(adjv)
                    stack.append(adjv)



customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }



g = Graph(customDict)
g.dfs("a")


