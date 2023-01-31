
def jump_ways(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
        
    '''
    Time Complexity - O(n)
    Space Complexity - O(n)
    '''
    # Write your code here.
    # if n==1 or n==2:
    #     return n
    # table = [-1]*(n+1)
    # table[1] = 1
    # table[2] = 2
    # for i in range(3,n+1):
    #     table[i] = table[i-1] + table[i-2]
    
    # return table[n]

    #Optimised version
    '''
    Time Complexity - O(n)
    Space Complexity - O(1)
    '''
    if n==1 or n==2:
        return n
    table = [-1]*3
    table[1] = 1
    table[2] = 2
    for i in range(3,n+1):
        if i%3==0:
            j = 0
        elif i%3==1:
            j=1
        elif i%3 ==2:
            j=2
        table[j] = table[(i-1)%3] + table[(i-2)%3]
    j = n%3
    return table[j]
    

print(jump_ways(4))



def ncr(n, r):
    """
    Args:
     n(int32)
     r(int32)
    Returns:
     int32
    """
    # Write your code here.
    
    #base case
    
    if r==0 or r==n:
        return 1
    
    table = [[0 for i in range(r+1)] for j in range(n+1)]
    #fill values for diagonal
    for i in range(r+1):
        table[i][i] =1
    #fill values for terminal nodes
    for i in range(n+1):
        table[i][0] = 1
        
    for i in range(2,n+1):
        for j in range(1,min(r+1,i+1)):
            table[i][j] = table[i-1][j] + table[i-1][j-1]
            
            
    return table[n][r]

# print(ncr(200,100))



def unique_paths(n, m):
    """
    Args:
     n(int32)
     m(int32)
    Returns:
     int32
    """
    # Write your code here.
    
    table = [[-1 for i in range(m)] for j in range(n)]
    
    #base case
    table[0][0] = 0
    for i in range(1,n):
        table[i][0] = 1
        
    for j in range(1,m):
        table[0][j] = 1
        
    
    #Iterative code
    for i in range(1,n):
        for j in range(1,m):
            table[i][j] = table[i][j-1] + table[i-1][j]
    
    return table[n-1][m-1]

print(unique_paths(3,2))