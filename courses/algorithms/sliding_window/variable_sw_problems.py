##-------------------------Problem -1-------------------------------
'''
209. Minimum Size Subarray Sum
'''

def minSubArrayLen(target: int, nums):
    
    
    global_cnt = len(nums)+1
    left = 0
    windowsum = 0
    for i in range(0,len(nums)):
        windowsum+=nums[i]
        while left <=i and windowsum>=target:
            global_cnt = min(global_cnt,i-left+1)
            windowsum-=nums[left]
            left+=1
    
    if global_cnt== len(nums)+1:
        return 0
    return global_cnt

# print(minSubArrayLen(nums= [2,3,1,2,4,3], target=7))


print(minSubArrayLen(target = 4, nums = [1,4,4]))


##-------------------------Problem -2-------------------------------
'''
713. Subarray Product Less Than K

'''
def numSubarrayProductLessThanK( nums, k: int) -> int:
    
    globalcnt = 0
    
    window_prod = 1
    
    left = 0
    for i in range(0,len(nums)):
        window_prod= window_prod*nums[i]
        while left<=i and window_prod>=k:
            window_prod = window_prod/nums[left]
            left+=1
        globalcnt+= i-left+1
    return globalcnt
print(numSubarrayProductLessThanK(nums=[10,5,2,6],k = 100))



##-------------------------Problem -4-------------------------------
'''
1004. Max Consecutive Ones III
'''
def longestOnes(nums, k: int) -> int:
    
    windowsum =0 
    globalsum = 0
    left = 0
    for i in range(0,len(nums)):
        if nums[i]==0:
            windowsum+=1
        
        while left<=i and windowsum>k:
            if nums[left]==0:
                windowsum-=1
            left+=1
        globalsum = max(globalsum,i-left+1)
        
    return globalsum

##-------------------------Problem -5-------------------------------
'''
904. Fruit Into Baskets
'''


def totalFruit( fruits) -> int:
    hmap = {}
    left = 0
    globalmax = 0
    for i in range(0,len(fruits)):
        if fruits[i] in hmap:
            hmap[fruits[i]]+=1
        else:
            hmap[fruits[i]]=1
        
        while left<=i and len(hmap)>2:
            hmap[fruits[left]]-=1
            if hmap[fruits[left]]==0:
                del hmap[fruits[left]]
            
            left+=1
        
        globalmax = max(globalmax,i-left+1)
    
    return globalmax
        
print("Total fruits",totalFruit([1,2,3,2,2]))



##-------------------------Problem -6-------------------------------
'''
longest-substring-with-at-most-two-distinct-characters
'''

def longestsubdistinct(arr):

    hmap = {}
    left = 0
    global_cnt = 0
    for i in range(0,len(arr)):
        if arr[i] in hmap:
            hmap[arr[i]]+=1
        else:
            hmap[arr[i]]=1
        
        while left<=i and len(hmap)>2:
            hmap[arr[left]]-=1
            if hmap[arr[left]]==0:
                del hmap[arr[left]]
            left+=1
        global_cnt = max(global_cnt,i-left+1)

    return global_cnt

print(longestsubdistinct("ccaabbb"))


##-------------------------Problem -7-------------------------------
'''
longest-substring-with-at-most-k-distinct-characters
'''
'''
Same as previous question 
Only change is Space Complexity is O(k+1) instead of O(3)
'''

def longestsubdistinctk(arr,k):

    hmap = {}
    left = 0
    global_cnt = 0
    for i in range(0,len(arr)):
        if arr[i] in hmap:
            hmap[arr[i]]+=1
        else:
            hmap[arr[i]]=1
        
        while left<=i and len(hmap)>k:
            hmap[arr[left]]-=1
            if hmap[arr[left]]==0:
                del hmap[arr[left]]
            left+=1
        global_cnt = max(global_cnt,i-left+1)

    return global_cnt

print("Longest Distinct k",longestsubdistinctk("ccaabbb",k=2))

##-------------------------Problem -8-------------------------------

def lengthOfLongestSubstring( arr: str) -> int:
    
    hmap = {}
    left = 0
    global_cnt = 0
    for i in range(0,len(arr)):
        if arr[i] in hmap:
            hmap[arr[i]]+=1
        else:
            hmap[arr[i]]=1
        #check with hmap[arr[i]] as it is the new entry in the hmap
        while left<=i and hmap[arr[i]]>1:
            hmap[arr[left]]-=1
            if hmap[arr[left]]==0:
                del hmap[arr[left]]
            left+=1
        global_cnt = max(global_cnt,i-left+1)

    return global_cnt


##-------------------------Problem -9-------------------------------
'''
1695. Maximum Erasure Value
'''

def maximumUniqueSubarray(nums) -> int:
    
    windowsum = 0
    left = 0
    hmap = {}
    globalsum = 0
    for i in range(0,len(nums)):
        windowsum+=nums[i]
        if nums[i] in hmap:
            hmap[nums[i]]+=1
        else:
            hmap[nums[i]]=1
        
        while left<=i and hmap[nums[i]]>1:
            windowsum-=nums[left]
            hmap[nums[left]]-=1
            if hmap[nums[left]]==0:
                del hmap[nums[left]]
            left+=1
        globalsum = max(globalsum,windowsum)
    return globalsum

print("maximumUniqueSubarray",maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))