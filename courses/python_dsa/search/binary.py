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