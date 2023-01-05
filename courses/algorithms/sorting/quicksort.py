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
