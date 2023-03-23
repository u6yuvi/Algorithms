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



##-------------------------Problem -3-------------------------------
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
        