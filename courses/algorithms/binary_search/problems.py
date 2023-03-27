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


'''
744. Find Smallest Letter Greater Than Target
'''

def nextGreatestLetter(letters, target: str) -> str:
    
    start = 0
    end = len(letters)-1
    
    while start<=end:
        mid = start + (end-start)//2
        
        if letters[mid]<=target:
            start  = mid +1
        elif letters[mid]>target:
            end = mid -1
    return letters[start%len(letters)]


'''
34. Find First and Last Position of Element in Sorted Array
'''

def searchRange(nums, target: int):
    
    # Find the leftmost pointer and then find the right most pointer
    
    start = 0
    end = len(nums)-1
    
    while start<=end:
        mid = start + (end-start)//2
        
        if nums[mid]<target:
            start = mid +1
        elif nums[mid]>=target:
            end = mid-1
        
    if start ==len(nums) or nums[start]!=target:
        return [-1,-1]
    left_index = start
    
    #find the rightmost index
    #use the same start index
    end = len(nums)-1
    
    while start<=end:
        mid = start + (end-start)//2
        
        if nums[mid]<=target:
            start = mid +1
        elif nums[mid]>target:
            end = mid-1
    right_index = end
    
    return [left_index,right_index]

'''
check-if-a-number-is-majority-element-in-a-sorted-array
'''

def searchRange(nums, target: int):
    
    # Find the leftmost pointer and then find the right most pointer
    
    start = 0
    end = len(nums)-1
    
    while start<=end:
        mid = start + (end-start)//2
        
        if nums[mid]<target:
            start = mid +1
        elif nums[mid]>=target:
            end = mid-1
        
    if start ==len(nums) or nums[start]!=target:
        return False
    left_index = start
    
    #find the rightmost index
    #use the same start index
    end = len(nums)-1
    
    while start<=end:
        mid = start + (end-start)//2
        
        if nums[mid]<=target:
            start = mid +1
        elif nums[mid]>target:
            end = mid-1
    right_index = end
    
    if right_index -left_index +1 > len(nums)/2:
        return True
    return False


'''
74. Search a 2D Matrix
'''

def searchMatrix(self, matrix, target: int) -> bool:
    
    start = 0
    rows = len(matrix)
    cols = len(matrix[0])
    
    end = (rows*cols) -1
    while start <=end:
        mid = start + (end-start)//2
        m = mid//cols
        n = mid%cols
        if matrix[m][n]==target:
            return True
        elif matrix[m][n] < target:
            start = mid +1
        else:
            end = mid -1
            
    return False