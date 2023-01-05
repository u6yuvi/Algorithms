def merge_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    
    def mergesort(arr,start = 0,end = len(arr)-1):
        if start == end:
            return
        
        mid = (start + end)//2
        mergesort(arr,start,mid)
        mergesort(arr,mid+1,end)
        merge_combine(arr,start,mid,end)
        return arr
 
    return mergesort(arr,0,len(arr)-1)


def merge_combine(arr,start,mid,end):
    i = start
    j = mid+1
    aux_arr = []
    while i<= mid and j <= end:
        if arr[i] <= arr[j]:
            aux_arr.append(arr[i])
            i+=1
        elif arr[i] > arr[j]:
            aux_arr.append(arr[j])
            j+=1
    while i<= mid:
        aux_arr.append(arr[i])
        i+=1
    while j <= end:
        aux_arr.append(arr[j])
        j+=1
    arr[start:end+1] = aux_arr
    return arr



# def helper(arr,start,mid,end):

#     aux_arr = []
#     i = start
#     j = mid +1

#     while i <= mid and j<= end:
#         if arr[i]<=arr[j]:
#             aux_arr.append(arr[i])
#             i+=1
#         elif arr[i]> arr[j]:
#             aux_arr.append(arr[j])
#             j+=1
    
#     while i<=mid:
#         aux_arr.append(arr[i])
#         i+=1
#     while j <=end:
#         aux_arr.append(arr[j])
#         j+=1
    
#     arr[start,end+1] = aux_arr
#     return arr


# def merge_sort(arr):

    
#     def merge(arr,start =0,end = len(arr)-1):

#         if start==end:
#             return
#         mid = (start + end)//2
#         merge(arr,start,mid)
#         merge(arr,mid+1,end)
#         helper(arr,start,mid,end)
#         return arr

        
#     return merge(arr,0,len(arr)-1)
        


if __name__ =="__main__":
   print(merge_sort([2,1,3,4]))