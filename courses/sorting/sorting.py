'''
Sorting Algorithms can be divided based on the following categories

1. Space used
    1. In place
    No extra space required - bubble Sort
    2. out of place - extra spsce is required - Merge Sort
2. Stability Based
    1. Stable - duplicate elements maintains the same order - Insertion Sort
    2. Unstable - duplicate elements changes the order of occurance - Quick Sort.



Terminologies in Sorting
1. Increasing Order
2. Decreasing order
3. Non Increasing Order - When duplicate elements exists
4. Non Decreasing Order - When duplicates elements exists.


Factors to consider while selecting a sorting algorithm
1. Stability 
2. Space Efficient
3. Time Efficient
'''

#Bubble Sort
'''
We repeatedly compare each pair of adjacent items 
and swap them if they are in the wrong order
'''

from pydoc import cli


def bubblesort(clist):
    '''
    Time Complexity - O(n^2)
    Space Complexirt - O(1)

    Advantages:
    1. Space efficient
    2. Easy to implement
    3. Ability to detect that the list 
    is sorted efficiently is built into the algorithm. 
    When the list is already sorted (best-case), the complexity
     of bubble sort is only O(n)

    Disadvantages:
    1. Average Time Complexity is high
    '''
    for i in range(len(clist)-1):
        for j in range(len(clist)-i-1):
            if clist[j] > clist[j+1]:
                clist[j] , clist[j+1] = clist[j+1], clist[j]

    return clist

#Selection Sort


def selectionsort(clist):
    '''
    we repeatedly find the minimum element and move it to the sorted part
     of array to make unsorted part sorted

    Time Complexity - O(n^2)
    Space Complexity - O(1)
    
    Advantages:
    1. Space efficient
    2. Easy to implement

    Disadvantages:
    1. Average Time Complexity is high

    '''
    for i in range(len(clist)):
        min_index = i
        for j in range(i+1,len(clist)): # find the smallest element
            if clist[min_index] > clist[j]:
                min_index = j 
        clist[i] , clist[min_index] = clist[min_index], clist[i] #replace with smallest
    return clist


#Insertion Sort

def insertionsort(clist):
    '''
    Divide the given array into two part
    Take first element from unsorted array and find its correct position in
    sorted array
    Repeat until unsorted array is empty
    Time Complexity - O(n^2)
    Space Complexity - O(1)
    Advantages:
    1. Space efficient
    2. Easy to implement
    3. Use when we have continuos inflow of numbers and 
    we want to keep them sorted

    Disadvantages:
    1. Average Time Complexity is high

    '''
    for i in range(1,len(clist)):
        key = clist[i]
        j = i-1
        while j>=0 and key<clist[j]:
            clist[j+1] = clist[j]
            j-= 1
        clist[j+1] = key
    return clist



def merge(arr,l,m,r):
    n1 = m-l +1
    n2 = r-m
    L = [0]* n1
    R = [0]*n2

    #copy elements from arr to sub array
    for i in range(0,n1):
        L[i] = arr[l+i]

    for j in range(0,n2):
        R[j] = arr[m+1+j]

    #set initial index to 0
    i = 0
    j = 0
    k = l
        
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    
    while i < n1:
        arr[k] = L[i]
        i+=1
        k+=1
    while j < n2:
        arr[k] = R[j]
        j+=1
        k+=1



def mergesort(arr,left_indx,right_indx):
    if left_indx<right_indx: # stopping condition
        # create two sub arrays
        m = (left_indx + (right_indx-1))//2
        mergesort(arr, left_indx,m)
        mergesort(arr,m,right_indx)
        merge(arr,left_indx,m,right_indx)
    return arr




if __name__=="__main__":
    assert bubblesort([2,1,23,4,3]) == [1,2,3,4,23]

    #print(selectionsort([2,1,23,4,3]))
    assert selectionsort([2,1,23,4,3]) == [1,2,3,4,23]

    print(insertionsort([2,1,23,4,3]))

    arr1 = [12, 11, 13, 5, 6, 7]
    #print(mergesort(arr1,0,len(arr1)-1))

    print(arr1[0:3],arr1[3:5])

    mid =(0 + len(arr1) -1-1) //2
    print(mid)

    print(arr1[0:mid],arr1[mid:])