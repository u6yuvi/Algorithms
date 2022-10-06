'''
Minimum cost to reach the last cell
Problem Statement:
- 2D Matrix is given
- Each cell has a cost associated with it for accessing
- We need to start from (0.0) cell and go till (n-1,n-1) cell - We can go only to right or down cell from current cell
- Find the way in which the cost is minimum
'''


def findMinCost(arr,row,col):
    #print("entering again",row,col)
    if row == -1 or col == -1:
        return float('inf')
    if row==0 and col ==0:
        return arr[row][col]
    else:
        option1 = findMinCost(arr,row,col-1)
        print("option1",option1,row,col)
        option2 = findMinCost(arr,row-1,col)
        print(row,col)
        print("return",option1,option2)
        print( "result" , arr[row][col] + min(option1,option2))
        return arr[row][col] + min(option1,option2)

TwoDList = [[4,7,8,6,4],
           [6,7,3,9,2],
           [3,8,1,2,4],
           [7,1,7,3,7],
           [2,9,8,9,3]
           ]

print(findMinCost(TwoDList, 4,4))

print(float('inf'))