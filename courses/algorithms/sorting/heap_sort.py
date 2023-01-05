
def heap_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    #Step-1 Heapify 
    #Step-2 Extract Max(Swap max with the last element)
    #Step3 - Heapify the swapped root element
    
    n = len(arr)
    no_levels = n//2
    
    def heapify(arr,n,i):
        print("in_heap",arr,n,i)
        largest = i
        l = 2*i+1
        r = 2*i +2
        if l<n and arr[largest] < arr[l]:
            print("l")
            largest = l
        if r < n and arr[largest] < arr[r]:
            print("r")
            largest = r
        
        if largest != i :
            print("swap")
            arr[largest], arr[i] = arr[i], arr[largest]
            heapify(arr,n,largest)
            
    #Step-1
    for i in range(no_levels,-1,-1):
        print("Heapify",i)
        print(arr,n,i)
        heapify(arr,n,i)
    #Step-2 Extract Max
    print("extract_max")
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0], arr[i]
        #Heapify root element
        heapify(arr,i,0)
    
        

    
    return arr


# def heapify(arr, n, i):
#     # Find largest among root and children
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#     if l < n and arr[i] < arr[l]:
#         largest = l
#     if r < n and arr[largest] < arr[r]:
#         largest = r
#     # If root is not largest, swap with largest and continue heapifying
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)

# def heap_sort(arr):
#     n = len(arr)
#     # Build max heap
#     for i in range(n // 2, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n - 1, 0, -1):
#         # Swap
#         arr[i], arr[0] = arr[0], arr[i]
#         # Heapify root element
#         heapify(arr, i, 0)
#     return arr

print(heap_sort([-10000,0,10000]))