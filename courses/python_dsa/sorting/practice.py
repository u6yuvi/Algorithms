
from re import L


def merge(arr,start,middle,end):
    n1 = middle-start +1
    n2 = end - middle

    L = [0]*n1
    R = [0]*n2
    for i in range(n1):
        L[i] = arr[start+i]

    print(start,middle,end)
    print("L",L)
    for j in range(n2):
        R[j] = arr[middle+1+j]

    print("R",R)
    i = 0
    j=0
    k = start

    while i <n1 and j <n2:
        if L[i] <=R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    
    print("index",i,j,k)
    while i < n1:
        arr[k] = L[i]
        i+=1
        k+=1
    
    while j <n2:
        arr[k] = R[j]
        j+=1
        k+=1




def mergesort(arr,start,end):
    '''
    # Divide and conquer algorithm 
    # keep dividing the array into two halves until the length is one
    # start merging the elements in a sorted manner
    # create two sub arrays L and R 
    #The algorithm maintains three pointers, one for each 
    # of the two arrays and one for maintaining the current index of the final sorted array.
    
    Have we reached the end of any of the arrays?
    No:
        Compare current elements of both arrays 
        Copy smaller element into sorted array
        Move pointer of element containing smaller element
    Yes:
        Copy all remaining elements of non-empty array
    '''
    print(f'Recursion',arr)
    if start < end :
        middle = (start + end)//2
        mergesort(arr,start,middle)
        mergesort(arr,middle+1,end)
        merge(arr,start,middle,end)
    return arr


# arr1 = [12, 11, 13, 5, 7, 6,14]
# print(mergesort(arr1,0,len(arr1)-1))



def partition(arr,start,end):
    pivot = arr[end]
    i = start -1
    for j in  range(start,end):
        if arr[j]< pivot:
            i = i+1
            arr[j] , arr[i] = arr[i],arr[j]
    arr[i+1], arr[end] = arr[end], arr[i+1]

    return i+1


def quicksort(arr,start,end):
    if start < end :
        pi = partition(arr,start,end)
        quicksort(arr,start,pi-1)
        quicksort(arr,pi+1,end)
    return arr


# arr1 = [12, 11, 13, 5, 7, 6]
# print(quicksort(arr1,0,len(arr1)-1))

def insertion(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1 # span of sorted array
        while j>=0 and key< arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
            

arr1 = [12, 11, 13, 5, 7, 6]
print(insertion(arr1))