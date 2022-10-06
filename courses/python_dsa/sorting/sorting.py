#References
#https://www.interviewkickstart.com/learn/comparison-among-bubble-sort-selection-sort-and-insertion-sort

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


from turtle import end_fill


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
    Logic
    1. Select an  element 
    2. Increase the span the sorted arry window untill that element
    3. keep shifting the element in the sorted array for placing the element
    4. add the sorted array with th element.
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


def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    #print(n1,n2,l,m,r)

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l+i]
    print("L",L)
    for j in range(0, n2):
        R[j] = customList[m+1+j]
    print("R",R)
    
    i = 0 
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

#Merge Sort - https://www.programiz.com/dsa/merge-sort
def mergeSort(customList, l, r):
    '''
    Time Complexity - O(nlogn)
    Space Complexity - O(n)
    '''
    print("Enter",customList)
    if l < r:
        m = (l+(r-1))//2
        mergeSort(customList, l, m)
        mergeSort(customList, m+1, r)
        merge(customList, l, m, r)
        print(customList)
    return customList



if __name__=="__main__":
    assert bubblesort([2,1,23,4,3]) == [1,2,3,4,23]

    #print(selectionsort([2,1,23,4,3]))
    assert selectionsort([2,1,23,4,3]) == [1,2,3,4,23]

    print(insertionsort([2,1,23,4,3]))
    arr1 = [12, 11, 13, 5, 7, 6]
    print(insertionsort(arr1))

    # arr1 = [12, 11, 13, 5, 7, 6]
    # print(mergeSort(arr1,0,len(arr1)-1))

    # print(arr1[0:3],arr1[3:5])

    # mid =(0 + len(arr1) -1-1) //2
    # print(mid)

    # print(arr1[0:mid],arr1[mid:])
