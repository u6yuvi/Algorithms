
def find_combinations_sum(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    def combinations(n,k):
        if n<=1 or k==0 or k==n:
            result.append([n,k])
            return 
        else:
            for k in range(0,n):
                return combinations(n-1,k-1) + combinations(n-1,k)
    #return [combinations(n,k)]
    result = []
    combinations(n,k)
    return result
print(find_combinations_sum(3,1))



def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    all_set = []
    def combinations(n,k):
        if n<=1 or k==0 or k==n:
            return []
        else:
            all_set.append([n,k])
            #all_set.append([n-1,k])
            combinations(n-1,k-1) + combinations(n-1,k)

        return all_set

    return combinations(n,k)

# print(find_combinations(5,2))

# [
# [1, 2],
# [1, 3],
# [1, 4],
# [1, 5],
# [2, 3],
# [2, 4],
# [2, 5],
# [3, 4],
# [3, 5],
# [4, 5]
# ]



def tower_of_hanoi(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    def towerofhanoi(n,src,aux,dest):
        if n==1:
            #print("Move a single disk from source to destination")
            result.append([src,dest])
        else:
            towerofhanoi(n-1,src,dest,aux)
            result.append([src,dest])
            #print("Moving n-1 disk from source to auxiliary place")
            towerofhanoi(n-1,aux,src,dest)
    result = []
    towerofhanoi(n,1,2,3)
    return result

# print(tower_of_hanoi(1))

# Binary String of length n
#["000", "001", "010", "011", "100", "101", "110", "111"]

def binary_string(n):


    def binary_helper(n,slate):
        if n==0:
            result.append(slate)
            return
        else:
            binary_helper(n-1,slate+"0")
            binary_helper(n-1,slate+"1")
        #return slate

    result = []
    slate = ""
    binary_helper(n,slate)
    return result

# print(binary_string(1))