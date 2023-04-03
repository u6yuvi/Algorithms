
'''
53. Maximum Subarray
'''
def maxSubArray(nums) -> int:
    
    globalsum = nums[0]
    prev_sum = nums[0]
    for i in range(1, len(nums)):
        prev_sum = max(prev_sum+nums[i],nums[i])
        globalsum = max(globalsum,prev_sum)
        
    return globalsum