'''
You have a web server that keeps crashing each day. 
You suspect it begins failing after a certain number of requests are served. 
Luckily, you have the daily request logs for the server. 
You see that it returns a status code of 200, but at some point it begins returning 500s instead:

In order to find the breaking point, let's write a function find_first(array, num) that returns the 
index at which the number num first appears in the input array. In this case, we want to efficiently 
find the first 500 in our server log.

input = [200, 200, 200, 200, 500, 500, 500]

find_first(input, 200) # => 0
find_first(input, 500) # => 4
find_first(input, 100) # => -1
'''


'''
Answer:
Two ways to solve it:
1 . When we find the number, explore each element to the left until we hit that number.
2. When we find the number, keep performing binary search on the left subtree until we can't find another .

Solution #1 seems like a reasonable idea, but #2 has much better worst-case performance. 
To see why, imagine our entire input was 500s; with Solution #1, we end up iterating over 
half of the list once we find the first 500, which is still O(N). In general, 
we should try to optimize this worst-case performance
'''

#Solution -1 
def search(arr,num):
    start = 0
    end = len(arr) -1
    mid = start + (end-start)//2
    while start < end  and arr[mid]!=num:
        if arr[mid] < num:
            start = mid +1
        elif arr[mid]> num:
            end = mid -1
        mid = start + (end-start)//2

    if arr[mid]==num:
        return mid
    return -1


def find_first(arr,num):           #  ~O(n) Worst case scenario
    found_index = search(arr,num)  #------- log(n)
    if found_index!=-1:
        first = found_index -1
        idx = found_index
    # to check is it a first index
        while first >=0:          #--------- n/2
            if arr[first] == arr[found_index]: 
                idx = first
            first-=1
        return idx
    return -1


arr= [200, 200, 200, 200, 500, 500, 500,600,700]
num = 200
print(F'Searching for {num}')
print("Search First - Solution-1",find_first([200, 200, 200, 200, 500, 500, 500],200))

#

def search_modified(arr,num):    #-------- O(log(n))
    start = 0
    end = len(arr)  # why not len(arr) -1
    idx = -1
    while start < end:
        #mid = int(start + (end - start) / 2) 
        mid = start + (end-start)//2 # same as above
        if arr[mid] == num:
            idx = mid
            end = mid
        
        elif arr[mid] < num:
            start = mid +1

        elif arr[mid]> num:
            end = mid

    return idx



arr= [200, 200, 200, 200, 500, 500, 500,600,700]
num = 200
print(F'Searching for {num}')
print("Search First - Solution 2",search_modified(arr,num))


# Find the last element of the array

def search_modified(arr,num):    #-------- O(log(n))
    start = 0
    end = len(arr)  # why not len(arr) -1
    idx = -1
    while start < end:
        #mid = int(start + (end - start) / 2) 
        mid = start + (end-start)//2 # same as above
        #print(start,mid,end)
        if arr[mid] == num:
            idx = mid
            start = mid + 1
        
        elif arr[mid] < num:
            start = mid +1

        elif arr[mid]> num:
            end = mid 

    return idx



arr= [200, 200, 200, 200, 500, 500, 500,600,700]
num = 200
print(F'Searching for {num}')
print("Search Last -",search_modified(arr,num))