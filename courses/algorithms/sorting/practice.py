import random

# Implement Merge Sort


def merge(a,start,mid, end):
    i = start
    j = mid+1
    aux_array = []
    while i <= mid and j<= end:
        if a[i] <= a[j]:
            aux_array.append(a[i])
            i+=1
        elif a[i]> a[j]:
            aux_array.append(a[j])
            j+=1
    
    while i<=mid:
        aux_array.append(a[i])
        i+=1
    
    while j<= end:
        aux_array.append(a[j])
        j+=1
    a[start:end+1] = aux_array
    #return a






def merge_sort(a,start,end):

    #base case
    if start==end:
        return 

    else:
        mid = start + (end-start)//2
        merge_sort(a,start,mid)
        merge_sort(a,mid+1,end)
        merge(a,start,mid,end)
        return a
    

a = [2,1,3,4,7,5]
# print(merge_sort(a,0,len(a)-1))


#Quick Sort

def quick_sort(a,start,end):

    #base case 
    if start >=end:
        return 

    
    #get the pivot element 
    pivot_idx = random.randint(start,end)

    #swap
    a[start] , a[pivot_idx] = a[pivot_idx] , a[start]

    #lomuto's parttioning
    smaller = start
    for bigger in range(start+1,end+1):
        if a[bigger]< a[start]:
            smaller+=1
            a[smaller] , a[bigger] = a[bigger], a[smaller]

    #swap
    a[start] , a[smaller] = a[smaller], a[start]

    quick_sort(a,start,smaller-1)  #excluding the pivot element
    quick_sort(a,smaller+1,end)
    return a

# print(quick_sort(a,0,len(a)-1))


#Group numbers even and odd

a = [1,2,3,7,4]

def group_numbers(a):
    smaller = -1
    for bigger in range(0,len(a)):
        if a[bigger]%2==0:
            smaller+=1
            a[bigger], a[smaller] = a[smaller],a[bigger]
    return a

print(group_numbers(a))
