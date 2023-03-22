##-------------------------Problem -1-------------------------------
'''
346 . Moving-average-from-data-stream
'''

def moving_avg_data_stream():

    #initialisation
    q = []
    totalsumsofar = 0

    # incoming stream of data
    new_val = 2
    k = 5 #window size
    totalsumsofar+=new_val
    q.append(new_val)
    if len(q)>k:
        totalsumsofar-= q.pop(0)
    
    return totalsumsofar/len(q)


#-------------------Problem-2--------------------------------
'''
643. Maximum Average Subarray I
'''

def findMaxAverage(nums, k) -> float:
    
    # Decrease and Conquer Approach
    '''
    Step -1 Initalise metrics/numbers for the leftmost window

    Step-2 Lazy manager 
    for i in range(k,n):
        - Update the window and its metrics 
            Add the rightmost element
            Subtract the leftmost element
        - Update the global answer based on local answer
        
    '''
    '''
    T(n) = O(n)
    Space = O(1)

    #However Brute Force approach =T(n) - O(nk)
    '''

    window_sum = sum(nums[0:k])
    
    max_sum = window_sum
    
    for i in range(k,len(nums)):
        window_sum+=nums[i] - nums[i-k] #1st element of the previous window
        if window_sum > max_sum:
            max_sum = window_sum
            
    return float(max_sum/k)


print(findMaxAverage([1,12,-5,-6,50,3], k = 4))

#-------------------Problem-3---------------------------------
'''
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
'''
def numOfSubarrays(arr, k, threshold) -> int:

    # Decrease and Conquer Approach
    '''
    Step -1 Initalise metrics/numbers for the leftmost window

    Step-2 Lazy manager 
    for i in range(k,n):
        - Update the window and its metrics 
            Add the rightmost element
            Subtract the leftmost element
        - Update the global answer based on local answer
        
    '''
    
    global_cnt = 0
    window_sum = sum(arr[0:k])
    if window_sum/k >=threshold:
        global_cnt+=1
        
    for i in range(k,len(arr)):
        window_sum+=arr[i]-arr[i-k]
        if window_sum/k>=threshold:
            global_cnt+=1
    
    return global_cnt

#---------------------Problem-4----------------------------
'''
Diet-plan-performance
T(n) = O(n)
Space = O(1)
'''

def diet_plan(arr,k,lower,upper):
    window_sum = sum(arr[0:k])
    global_cnt = 0
    if window_sum>upper:
        global_cnt+=1
    elif window_sum<lower:
        global_cnt-=1

    for i in range(k,len(arr)):
        window_sum+=arr[i]-arr[i-k]
        if window_sum>upper:
            global_cnt+=1
        elif window_sum<lower:
            global_cnt-=1
    return global_cnt


print(diet_plan([1,2,3,4,5], k = 1, lower = 3, upper = 3))


#-------------------Problem-5------------------------------
'''
1052. Grumpy Bookstore Owner

Optimisation problem - Optimise for dissatisfied customers.

# Identify the window sum whhere maximum  number of dissatisifed customer got converted \
into satisfied.
Add it to the satisfied customer count to get the final result.

'''
def maxSatisfied(customers, grumpy, minutes: int) -> int:
    angry = 0
    for i in range(0,minutes):
        if grumpy[i]==1:
            angry+=customers[i]
            
    satisfied = 0
    for j in range(0,len(customers)):
        if grumpy[j] ==0:
            satisfied+=customers[j]
    
    global_max = angry
    for i in range(minutes,len(customers)):
        if grumpy[i]==1:
            angry+=customers[i]
        if grumpy[i-minutes]==1:
            angry-=customers[i-minutes]
        global_max = max(global_max,angry)
        
    
    return global_max + satisfied

#--------------------Problem-6---------------------------------------
'''
1456. Maximum Number of Vowels in a Substring of Given Length
'''

def maxVowels(s: str, k: int) -> int:
    
    max_count = 0
    vowel = {"a","e","i","o","u"}
    for i in range(0,k):
        if s[i] in vowel:
            max_count+=1
    
    global_cnt = max_count
    for i in range(k,len(s)):
        if s[i] in vowel:
            max_count+=1
            
        if s[i-k] in vowel:
            max_count-=1
            
        global_cnt = max(global_cnt,max_count)
        
    return global_cnt


assert maxVowels(s = "abciiidef",k=3) ==3 , "Max-vowel- should be 3"


#--------------------Problem-7---------------------------------------

'''
1100. Find k length Substring with no repeated characters
'''

def substr_non_repeated(s,k):

    global_cnt = 0
    hmap = {}
    for i in range(0,k):
        if s[i] in hmap:
            hmap[s[i]]+=1
        else:
            hmap[s[i]]=1
    
    if len(hmap)==k:
        global_cnt+=1

    for i in range(k,len(s)):
        #add the last element
        if s[i] in hmap:
            hmap[s[i]]+=1
        else:
            hmap[s[i]]=1
        
        #remove the i-kth element
        hmap[s[i-k]]-=1
        #check if cnt of i-kth element is 0 
        if hmap[s[i-k]]==0:
            del hmap[s[i-k]]
        
        if len(hmap)==k:
            global_cnt+=1
    return global_cnt

print(substr_non_repeated(s = "havefunonleetcode",k=5))


#-----------------Problem-8-------------------------------
'''
239. Sliding Window Maximum
'''
def maxSlidingWindow( nums, k):
    
    '''
    T(n) = o(n)
    Space = O(k)
    '''
    '''
    Identify a transform method where insert , delete can happen in O(1)
    Also at any moment we know which is the max element in O(1)
    
    '''
    
    from collections import deque
    
    d =deque()
    result = []
    
    def pushin(val):
        '''
        while deque is not empty and back element < nums[i]
        remove the back element
        '''
        while d and d[-1]<val:
            d.pop()
        d.append(val)
    
    #fill an empty deque
    for i in range(0,k): 
        pushin(nums[i])
    
    #max is the front element of deque
    result = [d[0]]
        
    for i in range(k,len(nums)):
        '''
        Remove nums[i-k] and add nums[i] 
        if nums[i-k] is the front element of the deque,
            remove it from deque
        else if would already have been eliminated
        
        while deque is not empty and back element < nums[i]
        remove the back element
        
        push nums[i] to the back of the deque
        '''
        if d[0]==nums[i-k]:
            d.popleft()
        pushin(nums[i])
        result.append(d[0])
        
    return result

print("Max-sliding-window" , maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7] , k =3))