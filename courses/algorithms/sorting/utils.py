def binary_search(arr,search):
    start = 0
    end = len(arr)-1
    mid = start + (end - start)//2
    while arr[mid]!=search and start < end:
        if arr[mid]>=search:
            end = mid -1
        elif arr[mid] < search:
            start = mid +1
        mid = start + (end -start)//2
    
    if arr[mid] == search:
        return mid
    
    return -1


# print(binary_search([2,1,3,4],4))