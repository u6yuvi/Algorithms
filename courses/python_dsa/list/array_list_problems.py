#Given 2D list calculate the sum of diagonal elements.

#Example
 
def sumDiagonal(a):
    sumd = 0
    rows = len(a)
    cols = len(a[0])
    for i in range(rows):
        sumd +=a[i][i]
    return sumd
                
'''
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
firstSecond(myList) # 90 87
'''
def firstSecond(given_list):
 
    a = given_list   #make a copy
 
    a.sort(reverse=True)
 
    print(a)
 
    first = a[0]
 
    second = None
 
    for element in given_list:
 
        if element != first:
 
            second = element
 
            return first, second

'''
Missing Number
Write a function to find the missing number in a given integer array of 1 to 100.

Example

missingNumber([1, 2, 3, 4, 6], 6) # 5
'''
def missingNumber(myList, totalCount):
    expectedSum = totalCount * ((totalCount + 1) / 2)
    actualSum = 0
    for i in myList:
        actualSum += i
    return int(expectedSum - actualSum)

'''
Duplicate Number
Write a function to find the duplicate number on given integer array/list.

Example

removeDuplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
'''
def removeDuplicates(myList):
    new_list=[]
 
    for i in myList:
 
        if i not in new_list:
 
            new_list.append(i)
 
    return new_list



def pairSum(myList,sum):
    #myList.sort()
    new_list = []
    i = 0
    while i <len(myList):
        j = 1
        while j < len(myList):
            if myList[i] + myList[j] ==sum:
                sum1 = str(myList[i]) + str("+") +str(myList[j])
                if sum1 not in new_list:
                    new_list.append(sum1)
            j +=1
        i +=1
    return new_list
        
if __name__=="__main__":
    myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
    assert sumDiagonal(myList2D) == 15


    print(pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))

    my_dict = {}
    my_dict[(1,2,4.2)] = 8
    my_dict[(4,2,1)] = 10
    my_dict[(1,2)] = 12
    my_dict[4.2] = 60
    
    sum = 0
    for k in my_dict:
        print(my_dict.keys())

    my_dict = {}
    my_dict[4] = 2
    my_dict[4.0] = 2
    print(my_dict)