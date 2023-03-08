import random
def quicksort(arr,start, end):


    if start>=end:
        return 
    
    #get the pivot element
    pivot = random.randint(start,end)
    arr[start] , arr[pivot] = arr[pivot], arr[start]

    #inplace operation to find the median(lomuto's partioning)
    smaller = start
    for bigger in range(start+1, end+1):
        if arr[bigger] < arr[smaller]:
            smaller+=1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
        
    #swap the 1st element with the last element of smaller subarray 
    arr[start],arr[smaller] = arr[smaller], arr[start]

    # conquer step
    quicksort(arr,start,smaller-1)
    quicksort(arr,smaller+1,end)
    return arr


a = [2,1,4,5,-2,5]
print(quicksort((a),0,len(a)-1))

print(str(quicksort((a),0,len(a)-1)))

def top_k_frequent(arr,k):
    hashmap = {}
    for i in range(0,len(arr)):
        if arr[i] in hashmap:
            hashmap[arr[i]] +=1
        else:
            hashmap[arr[i]] =1

    def quickselect(arr,start,end,k):
        if start == end:
            return 
        pivot = random.randint(start,end)
        arr[start],arr[pivot] = arr[pivot], arr[start]
        smaller = start
        for bigger in range(start+1, end+1):
            if arr[bigger]<=arr[start]:
                smaller+=1
                arr[bigger],arr[smaller] = arr[smaller],arr[bigger]
        
        arr[start], arr[smaller] = arr[smaller], arr[start]

        if arr[smaller]== len(arr)-k:
            print(arr[smaller:])
        elif arr[smaller] < len(arr)-k:
            quickselect(arr,smaller+1,end,k)
        else:
            quickselect(arr.smaller-1,end,k)
    quickselect(arr,0,len(arr)-1,k)

arr = [1, 2, 3, 2, 4, 3, 1]
# top_k_frequent(arr,2)

def top_k_freq(arr,k):
    hashmap = {}
    for i in range(0,len(arr)):
        if arr[i] in hashmap:
            hashmap[arr[i]] +=1
        else:
            hashmap[arr[i]] =1
    
    def quickselect(arr,start,end,k,hahsmap):
        if start==end: # smallest subproblem will always be of size 1.
            return 
        
        #pivot 
        pivot = random.randint(start,end)
        arr[start],arr[pivot] = arr[pivot],arr[start]
        #lomutos
        smaller = start
        for bigger in range(start+1,end+1):
            if hashmap[arr[bigger]] <= hashmap[arr[start]]:
                smaller+=1
                arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
        
        arr[smaller],arr[start] = arr[start], arr[smaller]
        
        if smaller==len(arr)-k:
            return 
        elif smaller < len(arr)-k:
            quickselect(arr,smaller+1,end,k,hashmap)
        else:
            quickselect(arr,start,smaller-1,k,hashmap)
            
    
    quickselect(arr,0,len(arr)-1,k,hashmap)
    return arr[len(arr)-k:]

