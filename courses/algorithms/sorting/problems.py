from merge_sort import merge_sort
from utils import binary_search
import random
import math

#----------------1st solution---------------------
#Presort + Binary Search
#T(n) = O(nlogn) + O(nlogn)

# def two_sum(arr,target):

#     sorted_array = merge_sort(arr)
#     for i in arr:
#         mid = binary_search(arr,target - i)
#         if  mid!=-1:
#             return (i,arr[mid])


# print(two_sum([2,1,5,7],6))

#------------------2nd Solution---------------------

#Presort + Two pointer 
    
def two_sum(arr,target):

    sorted_array = merge_sort(arr)
    
    i = 0
    j = len(arr)-1
    while i < j:
        print("i",i,j)
        #print(i,j)
        sum1 = arr[i] + arr[j]
        if sum1 == target:
            return True
        elif sum1 <=target:
            i+=1
        elif sum1>target:
            j-=1

# print(two_sum([2,1,5,7],6))

#--------------3rd Solution------------------

#Hash Map


#-------------3sum problem--------------------

def find_3_sum(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_str
    """
    # Write your code here.
    
    #Presort
    
    #QUICKSORT
    
    
        
    def quicksort(arr,start,end):
        
        if start >= end:
            return
        
        pivot = random.randint(start,end)
        #swap thje pivot element to the 1st place
        arr[start],arr[pivot] = arr[pivot] , arr[start]
        
        #lumuto's partitioning
        
        smaller = start
        for bigger in range(start,end+1):
            if arr[bigger]<arr[start]:
                smaller+=1
                arr[bigger] , arr[smaller] = arr[smaller], arr[bigger]
        
        arr[smaller], arr[start] = arr[start], arr[smaller]
        
        quicksort(arr,start,smaller)
        quicksort(arr,smaller+1,end)
        
        return arr
    
    
    #sort the array
    res = {}
    sorted_array = quicksort(arr,0,len(arr)-1)
    for i in range(0,len(arr)-1):
        j= i+1
        k = len(arr)-1
        while j< len(arr) -1 and k >i  and j<k:
            if sorted_array[j] + sorted_array[k] +sorted_array[i] ==0:
                key = str(str(sorted_array[i])+","+str(sorted_array[j])+","+str(sorted_array[k])) 
                if key not in res:
                    res[key] = 1
                j+=1
                k-=1
                    
            elif abs(sorted_array[j] + sorted_array[k]) <abs(sorted_array[i]):
                j+=1
            else:
                k-=1
    return res

# arr =  [0, 0, 0, 0, 0, 0]
# print(find_3_sum(arr))



# Merge Sorted array


def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    ''' As they are sorted:
        1. We can compare the last element of each array and identify the smaller number.
        
    Using two pointer logic
    '''    
    index1 = len(first)-1
    index2 = len(second)-len(first)-1
    index_last = len(second)-1
    while index1>=0 and index2>=0:
        if first[index1] >=second[index2]:
            second[index_last] = first[index1]
            index_last-=1
            index1-=1
        elif first[index1] < second[index2]:
            second[index_last] = second[index2]
            index2-=1
            index_last-=1
        
    while index1>=0:
        second[index_last] = first[index1]
        index_last-=1
        index1-=1

    while index2>=0:
        second[index_last] = second[index2]
        index_last-=1
        index2-=1
    
    return second

# print(merge_one_into_another(first=[1, 3, 5],second = [2, 4, 6, 0, 0, 0]))




def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    start = 0
    end = len(numbers)-1
    
    while start<end:
        if numbers[end]%2 !=0:
            end-=1
        elif numbers[end]%2==0:
            numbers[end],numbers[start] = numbers[start],numbers[end]
            start+=1
    return numbers


# print(segregate_evens_and_odds([1,2,3,7]))

#-------Problem-------------------

#T(n) = O(n)
#S(n)= O(1)

def segregate_even_odd(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    pivot = -1
    for i in range(0,len(numbers)):
        if numbers[i]%2==0:
            pivot+=1
            numbers[pivot] , numbers[i] = numbers[i], numbers[pivot]
    return numbers

# print(segregate_even_odd([1,2,3,4]))


#--------kth largest element---------------

def partition(arr,start,end):
    pivot = random.randint(start,end)
    print("pivot",pivot)
    arr[start] , arr[pivot] = arr[pivot], arr[start]
    
    
    smaller = start
    for bigger in range(start+1, end+1):
        if arr[bigger] < arr[start]:
            smaller+=1
            arr[smaller] , arr[bigger] = arr[bigger] , arr[smaller]
    
    arr[start] , arr[smaller] = arr[smaller], arr[start]
    return smaller


def kthlargest(arr,k):

    def quick_select(arr,start,end,k):

        if start==end:
            return 
        
        #get the pivot and replace it with the median value position in the array
        smaller = partition(arr,start,end)
        

        if smaller == len(arr)-k:
            return 
        elif smaller < len(arr) - k:
            quick_select(arr,smaller+1,end,k)
        else:
            quick_select(arr,0,smaller-1,k)
    
    
    
    quick_select(arr,0,len(arr)-1,k)
    return arr[len(arr)-k]  #return the element at the index (n-k)

# print(kthlargest([2],1))



def kth_largest_in_an_array(numbers, k):
    """
    Args:
     numbers(list_int32)
     k(int32)
    Returns:
     int32
    """
    # Write your code here.
    '''
    Quick Select Algorithm
    
    Kth largest element will at the place n-kth position in the array
    '''
    
    def quick_select(arr,start,end,k):
        if start==end:
            return
        
        pivot = random.randint(start,end)
        arr[pivot] , arr[start] = arr[start], arr[pivot]
        
        #lumuto's partitioning
        smaller = start
        for bigger in range(start,end+1):
            if arr[bigger] < arr[start]:
                smaller+=1
                arr[bigger], arr[smaller] = arr[smaller], arr[bigger]
            
        arr[start], arr[smaller] = arr[smaller] , arr[start]
            
        if smaller ==len(arr)-k:
            return 
        elif smaller < len(arr)-k:
            quick_select(arr,smaller+1,end,k)
        else:
            quick_select(arr,start,smaller-1,k) 
    
    quick_select(numbers,0,len(numbers)-1,k)
    return numbers[len(numbers)-k]

# print(kth_largest_in_an_array([5, 1, 10, 3, 21],2))


#---------------kth smallest element in the array---------------------
def kth_smallest_in_an_array(numbers, k):
    """
    Args:
     numbers(list_int32)
     k(int32)
    Returns:
     int32
    """
    # Write your code here.
    '''
    Quick Select Algorithm
    
    Kth smallest element will at the place k-1th position in the array
    '''
    
    def quick_select(arr,start,end,k):
        if start==end:
            return
        
        pivot = random.randint(start,end)
        arr[pivot] , arr[start] = arr[start], arr[pivot]
        
        #lumuto's partitioning
        smaller = start
        for bigger in range(start,end+1):
            if arr[bigger] < arr[start]:
                smaller+=1
                arr[bigger], arr[smaller] = arr[smaller], arr[bigger]
            
        arr[start], arr[smaller] = arr[smaller] , arr[start]
            
        if smaller ==k-1:
            return 
        elif smaller < k-1:
            quick_select(arr,smaller+1,end,k)
        else:
            quick_select(arr,start,smaller-1,k) 
    
    quick_select(numbers,0,len(numbers)-1,k)
    return numbers[k-1]

print(kth_smallest_in_an_array([5, 1, 10, 3, 21],2))


#----------------kth closest point to the origin----------------

def euclid(arr1,arr2):
    return math.sqrt((arr1[0]-arr2[0])**2 + (arr1[1]-arr2[1])**2)

def k_closest_points_to_the_origin(numbers, k):
    """
    Args:
     numbers(list_int32)
     k(int32)
    Returns:
     int32
    """
    # Write your code here.
    '''
    Quick Select Algorithm
    
    Kth smallest element will at the place k-1th position in the array
    '''
    
    def quick_select(arr,start,end,k):
        if start==end:
            return
        
        pivot = random.randint(start,end)
        arr[pivot] , arr[start] = arr[start], arr[pivot]
        
        #lumuto's partitioning
        smaller = start
        for bigger in range(start,end+1):
            if euclid(arr[bigger],[0,0]) < euclid(arr[start],[0,0]):
                smaller+=1
                arr[bigger], arr[smaller] = arr[smaller], arr[bigger]
            
        arr[start], arr[smaller] = arr[smaller] , arr[start]
            
        if smaller ==k-1:
            return 
        elif smaller < k-1:
            quick_select(arr,smaller+1,end,k)
        else:
            quick_select(arr,start,smaller-1,k) 
    
    quick_select(numbers,0,len(numbers)-1,k)
    return numbers[:k-1+1] # all elements upto kth element

print(k_closest_points_to_the_origin([[3,3],[5,-1],[-2,4]],2))


#-----------------Dutch Flag Sort-------------------------

def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    # Write your code here.

    '''
    Decrease and Conquer Approach with bottom up approach
    Think of the task done by all the subordinates and for the case n-1 , we assume we haven been
    provided with the red and the white index ,swap the elements based on certain conditions.
    
    Time Complexity - O(n)
    '''
    
    
    red = -1
    green = -1
    for i in range(0,len(balls)):
        if balls[i] == "G":
            green+=1
            balls[green] ,balls[i]= balls[i],balls[green]
            
        elif balls[i] == "R":
            green+=1
            balls[green] , balls[i] = balls[i], balls[green]
            red+=1
            balls[red] , balls[green] = balls[green] , balls[red]
            
    return balls


# print(dutch_flag_sort(["G", "B", "G", "G", "R", "B", "R", "G"]))


#---------------Intersection of 3 sorted arrays------------------

def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    i = 0
    j = 0
    k = 0
    res = []
    while i<len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] ==arr2[j] ==arr3[k]:
            res.append(arr1[i])
        min1 = min(arr1[i],arr2[j])
        min2 = min(min1,arr3[k])
        if min2 ==arr1[i]:
            i+=1
        if min2 == arr2[j]:
            j+=1
        if min2 == arr3[k]:
            k+=1
            
    if res:
        return res
    return [-1]

a = {
"arr1": [2, 5, 10],
"arr2": [2, 3, 4, 10],
"arr3": [2, 4, 10]
}
# print(find_intersection(a["arr1"],a["arr2"],a["arr3"])) #output [2,10]

#--------------Union of 3 sorted arrays----------------------   yet to be solved
def find_union(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    i = 0
    j = 0
    k = 0
    res = []
    while i<len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] ==arr2[j] ==arr3[k]:
            res.append(arr1[i])

        # elif (arr1[i] !=arr2[j]) or (arr2[j] !=arr3[k]) or (arr1[i]!=arr3[k]):
        #     res.append(arr1[i])
        #     res.append(arr2[j])
        #     res.append(arr3[k])
        min1 = min(arr1[i],arr2[j])
        min2 = min(min1,arr3[k])
        if min2 ==arr1[i]:
            res.append(arr1[i])
            i+=1
        if min2 == arr2[j]:
            res.append(arr2[j])
            j+=1
        if min2 == arr3[k]:
            res.append(arr3[k])
            k+=1
            
    #Gather the remaining element
    while i<len(arr1):
        res.append(arr1[i])
        i+=1
    while j<len(arr2):
        res.append(arr2[j])
        j+=1
    while k<len(arr3):
        res.append(arr3[k])
        k+=1

    if res:
        return res
    return [-1]

a = {
"arr1": [2, 5, 10],
"arr2": [2, 3, 4, 10],
"arr3": [2, 4, 10]
}

print("Union",find_union(a["arr1"],a["arr2"],a["arr3"])) #output [2,10]


#------------k most frequent words-------------------

def find_top_k_frequent_elements(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    hash_map = {}
    for i in range(0,len(arr)):
        if arr[i] in hash_map:
            hash_map[arr[i]] +=1
        else:
            hash_map[arr[i]] =1
    
    def quickselect(arr1,start,end,k,hash_map):
        if start==end:
            return
    

        pivot = random.randint(start,end)
        arr1[start], arr1[pivot] = arr1[pivot], arr1[start]
        
        smaller = start
        for bigger in range(start,end+1):
            if hash_map[arr1[bigger]]<hash_map[arr1[start]]:
                smaller+=1
                arr1[smaller], arr1[bigger] = arr1[bigger], arr1[smaller]
        arr1[smaller], arr1[start] = arr1[start], arr1[smaller]
        
        if smaller==len(arr1)-k:
            return
        elif smaller < len(arr1) - k:
            quickselect(arr1,smaller+1,end,k,hash_map)
        elif smaller > len(arr1) - k:
            quickselect(arr1,start,smaller-1,k,hash_map)
    
    arr1 = list(hash_map.keys())
    quickselect(arr1,0,len(arr1)-1,k,hash_map)
    
    
    print(hash_map)  
    print(arr1)  
    return arr1[len(arr1)-k:]

print(find_top_k_frequent_elements( [1, 2, 3, 2, 4, 3, 1],2))