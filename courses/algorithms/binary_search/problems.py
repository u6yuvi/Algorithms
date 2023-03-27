'''
704. Binary Search
'''

def search( nums, target: int) -> int:
    
    
    start = 0
    end  = len(nums)-1
    
    while start <= end:
        mid = start + (end-start)//2
        
        if nums[mid]==target:
            return mid
        elif nums[mid] > target:
            end = mid -1
        else:
            start = mid+1
    
    return -1


'''
374. Guess Number Higher or Lower
'''
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
# '''
def guessNumber( n: int) -> int:
    
    start = 1
    
    end = n
    
    while start <= end:
    
        mid = start + (end-start)//2
        val = guess(mid)
        if val ==0:
            return mid
        elif val ==-1:
            end = mid-1
        else:
            start = mid +1

'''
278. First Bad Version
'''
'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
'''

def firstBadVersion(n: int) -> int:
    
    start = 1
    
    end = n
    
    while start<=end:
        mid = start + (end-start)//2
        
        if isBadVersion(mid):
            end = mid-1
        else:
            start = mid +1
            
    #At this point , start is one more than the end
    #end points to the 1st good version
    #start points to the 1st bad version 
    #we get the boundary where good changes to bad
    return start

'''
35. Search Insert Position
'''
def searchInsert( nums, target: int) -> int:
    
    start = 0
    end = len(nums)-1
    
    while start<=end:
        mid = start + (end-start)//2
        
        if nums[mid]==target:
            return mid
        elif nums[mid] < target:
            start = mid+1
        else:
            end = mid-1
        
    return start