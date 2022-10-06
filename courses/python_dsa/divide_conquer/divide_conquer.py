# Number Factor
'''
Given N, find the number of ways to express N as a sum of 1, 3 and 4.

F(5) = (1,4) (4,1) (1,1,3) (3,1,1) (1,1,1,1,1)  5 ways

F(4) = (1,3) (1,1,1,1) (4) - 3ways
F(3) = (1,1,1) (3) - 2ways
F(2) =  (1,1) 1 way
F(1) = (1) 1way
#Divide into subproblems
 F(5) = F(4) +1  + F(2) +3 + F(1) + 4
 F(n) = F(n-1) +1 + F(n-3) + 3 + F(n-4) + 4
 '''

def factor(n):
    if n in [0,1,2]:
        return 1
    if n==3:
        return 2
    else:
        sub1 = factor(n-1)
        sub2 = factor(n-3)
        sub3 = factor(n-4)
    return sub1 + sub2 + sub3
N= 5
print(f'Number of factors of {N} is {factor(N)}')

'''
House Robber
Problem Statement:
- Given N number of houses along the street with some amount of money - Adjacent houses cannot be stolen
- Find the maximum amount that can be stolen
'''
'''
Eg: 5 houses
1st way - Select or reject 1s house

When select 1st house - sum 1st house + 
select1sthouse = cuurent + max(houses,currenthouse+2)
strategy2 = current+1 + max(houses, )
max(strategy1,stragety2)
'''

def houseRobber(houses,currentindex):
    if currentindex >= len(houses):
        return 0
    else:
        selecthouse1 = houses[currentindex] + houseRobber(houses,currentindex+2)
        skiphouse1 = houseRobber(houses,currentindex+1)
        return max(selecthouse1,skiphouse1)

assert houseRobber([6,7,1,30,8,2,4],0) == 41

#Convert one string to another
'''
Problem Statement:
- S1 and S2 are given strings
- Convert S2 to S1 using delete, insert or replace operations - Find the minimum count of edit operations
s1 = catch
s2 = carch
output = 1

S1 = “table”
- S2 = “tbres”
- Output = 3
Insert 
'''