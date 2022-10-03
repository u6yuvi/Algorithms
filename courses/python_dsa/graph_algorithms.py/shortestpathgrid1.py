from collections import deque


#Logic
'''
1. enqueue starting vertex
2. while queue is not empty
3.  cur = dequeue()
3.  add curr to visited 
4.  Identify the set of next vertices of curr
5.  Enqueue all the next adjacent vertices 
7.  update parent of adjecent vertices to curr
 '''

class Node:
    def __init__(self,x,y,parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def __repr__(self,):
        return str((self.x,self.y))


# steps in each direction to explore
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

def isValid(x,y,N):
    return 0<=x <N and 0<=y <N 

def getPath(curr,path = []):
    if curr:
        getPath(curr.parent,path)
        path.append(curr)


def findpath(matrix,start =0,end = 0):
    q = deque()
    visited = []
    q.append(Node(start,end))
    visited.append((start,end))

    while q:
        curr = q.popleft()

        if curr.x == len(matrix) -1 and curr.y == len(matrix) -1 :
            path = []
            getPath(curr,path)
            return path
        
        
        for i in range(len(row)):
            x = curr.x + row[i]* matrix[curr.x][curr.y]
            y = curr.y + col[i] * matrix[curr.x][curr.y]

            #check if x & y are valid
            if isValid(x,y,len(matrix)):
                next = Node(x,y,curr)

                if next not in visited:
                    visited.append((next.x,next.y))
                    q.append(next)



if __name__ == '__main__':
 
    matrix = [
        [4, 4, 6, 5, 5, 1, 1, 1, 7, 4],
        [3, 6, 2, 4, 6, 5, 7, 2, 6, 6],
        [1, 3, 6, 1, 1, 1, 7, 1, 4, 5],
        [7, 5, 6, 3, 1, 3, 3, 1, 1, 7],
        [3, 4, 6, 4, 7, 2, 6, 5, 4, 4],
        [3, 2, 5, 1, 2, 5, 1, 2, 3, 4],
        [4, 2, 2, 2, 5, 2, 3, 7, 7, 3],
        [7, 2, 4, 3, 5, 2, 2, 3, 6, 3],
        [5, 1, 4, 2, 6, 4, 6, 7, 3, 7],
        [1, 4, 1, 7, 5, 3, 6, 5, 3, 4]
    ]
 
    # Find a route in the matrix from source cell (0, 0) to
    # destination cell (N-1, N-1)
    path = findpath(matrix)
 
    if path:
        print('The shortest path is', path)
    else:
        print('Destination is not found')