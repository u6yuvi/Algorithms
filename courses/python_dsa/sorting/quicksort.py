
def partition(arr,start,end):
    pivot = arr[end] #last element in the array 1st pointer
    i = start-1 # 2nd pointer
    for j in range(start,end): 
        #interchange smaller element than pivot with 2nd pointer
        if arr[j]< pivot:
            i+=1
            arr[j],arr[i] = arr[i],arr[j]
    
    arr[i+1],arr[end] = arr[end],arr[i+1] #the pivot element is swapped with the second pointer

    return i+1

        


def quicksort(arr,start,end):
    if start < end:
        pi = partition(arr,start,end)
        quicksort(arr,start,pi-1)
        quicksort(arr,pi+1  ,end)
    return arr


arr = [12,11,10,5,7,6]
print(quicksort(arr,0,5))