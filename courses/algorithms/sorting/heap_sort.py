
def heap_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    '''
    Step-1 Heapify 
        1. Bubble up the max element to form a max_heap
            for i in range(max_level,0)
                heapify(arr,i,total_elements)

            def heapify(arr,i,total_elements):
                fetch left child index
                fetch right child index
                largest = parent node index
                if l_child and r_child are less than total_elements
                    swap if any l_child or r_child is greater than parent element(i)
                    heapify(arr,new_parent,old_parent)

    #Step-2 Extract Max and put it at the last leaf node
    # (Swap max[root parent] with the last element)
        for in in range(bottom ,top):
            swap root_node with the last leaf node
    #Step3 - Heapify the root element
    '''
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