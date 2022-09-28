# Missing Number between 1 & 1000

def missing_number(arr):
    expected_sum = (max(arr)*(max(arr)+1))/2
    actual_sum = sum(arr)
    missing_num = expected_sum - actual_sum
    return missing_num



# Find pairs that sums to target
'''
[1,2,3,4] , 7->  [4,3]'''

def pair_sum(arr,target):
    pair_sum = []
    for i in range(len(arr)-1):
        pair_sum = arr[i] + arr[i+1]
        if pair_sum == target:
            return (arr[i],arr[i+1])

#Max product of two integers in an array

def maxproduct(arr):
    # prod = 0
    # for i in range(len(arr)-1):
    #     running_prod = arr[i]*arr[i+1]
    #     if running_prod > prod:
    #         prod = running_prod
    # return prod

    return max([ arr[i]* arr[i+1] for i in range(len(arr)-1)])

#Whether list has all unique values

def isuniue(arr):
    uniqu = []
    for i in arr:
        if i in uniqu:
            return False
        else:
            uniqu.append(i)
    return True



if __name__=="__main__":
    print(missing_number([1,2,3,5]))

    print(pair_sum([1,2,3,4],7))

    print(maxproduct([3,2,4,3,8,4]))

    print(isuniue([2,3,4,5,5]))

