#Question-1 - Find the Duplicates
'''
Given two sorted arrays arr1 and arr2 of passport numbers, 
implement a function findDuplicates that returns an array of all passport 
numbers that are both arrays. Note that the output array should be 
sorted in ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. 
Solve for two cases and analyze the time & space complexities of your 
solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 
is much bigger than arr1.
'''

arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]
#output: [3, 6, 7] # since only these three values are both in arr1 and arr2
# Given array is sorted

#brute force
def brute_find_duplicates(arr1, arr2):
  dup_elem = []
  for i in arr1:
    for j in arr2:
      if i==j:
        dup_elem.append(i)
  return dup_elem

# print(brute_find_duplicates(arr1,arr2))

#Case-1 when M~N
# Time Complexity - O(M+N)
# Space Complexity - O(N) where N<= M
def find_duplicates(arr1,arr2):
    i = 0
    j = 0
    dup = []
    while i<len(arr1) and j < len(arr2):
        print(i)
        if arr1[i] == arr2[j]:
            dup.append(arr1[i])
            i = i+1
            j = j+1
        elif arr1[i] < arr2[j]:
            i = i+1
        else:
            j = j+1
    return dup

# print(find_duplicates(arr1,arr2))

#Case-2 
#When M>>N

'''
Avoid traversing in the longer array linearly and use 
binary search for bigger array
'''
def binary_search(arr,val):
    start = 0
    end = len(arr) -1
    mid = start + (end-start)//2
    while start < end and arr[mid]!=val:
        #print(start,end)
        if arr[mid] < val:
            start = mid +1
        elif arr[mid] > val:
            end = mid -1
        mid = start + (end-start)//2
    if arr[mid] == val:
        return arr[mid]
    return -1

# print(binary_search(arr1,7))
# Time Complexity - O(N*log(M))
# Space Complexity - O(N)
def find_duplicates(arr1,arr2):
    i = 0 
    dup = []
    while i < len(arr1):
        if binary_search(arr2,arr1[i]) !=-1:
            dup.append(arr1[i])
        i = i+1
    return dup


print(find_duplicates(arr1,arr2))

