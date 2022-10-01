# binary Search


# [1,2,3,4,5,7]
# Find 5

def binarysearch(arr,val):
    start = 0
    end = len(arr) -1 
    #middle = (start +end)//2
    middle = start + (end-start)//2 # to overcome overflow problem in int
    #https://algotree.org/algorithms/binary_search/
    print(start,middle,end)
    while arr[middle] != val and start < end:
        if arr[middle] >= val:
            end = middle-1
        elif arr[middle] <= val:
            start= middle+1
        #middle = (start + end)//2
        middle = start + (end - start)//2
        print(start,middle,end)
    
    if arr[middle]==val:
        return middle
    return -1

print(binarysearch([1,2,3,4,5,7],7))


#Counting duplicates

a = [1,2,2,3,3,4]

b = dict()
def countduplicates(arr,target):
    #Time Complexity - O(n)
    for i in arr:
        if i in b:
            b[i]+=1
        else:
            b[i] = 1
    if target in b:
        return b[target]
    return -1
        
print(countduplicates([1,2,2,2,3,3,4],2))

#Count Duplicates with Binary Search

def first(arr,target):
    start = 0
    end = len(arr) -1
    

    while start <= end:
        middle = start + (end-start)//2
        if arr[middle] == target:
            if (middle -1>=0 and arr[middle-1]==target):
                end = middle -1
                continue
            return middle
        elif arr[middle] < target:
            start = middle +1
        else:
            end = middle -1
    return -1


def last(arr,target):
    # find middle == target
    # go on increasing middle until arr[middle] == target
    start = 0
    end = len(arr) -1
    while start <= end:
        middle = start + (end-start)//2
        if arr[middle] == target:
            if middle +1 <len(arr) and arr[middle+1]==target:
                start = middle +1
                continue
            return middle

        if arr[middle]<target:
            start = middle +1
        else:
            end = middle -1
    
    return -1 
print(first([1,2,2,2,3],2))

print(last([1,2,2,2,3,3],2))
