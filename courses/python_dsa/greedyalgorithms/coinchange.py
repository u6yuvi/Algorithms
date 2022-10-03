'''
You are given coins of different denominations and total amount of money. 
Find the minimum number of coins that you need yo make up the given amount.
Infinite supply of denominations : {1,2,5,10,20,50,100,1000}
'''

#PseudoCode
'''
1. Sort the denominations in descending order.
2. Select 1st coin as currcoin 
2. while remaining amount !=0:
    if remaining_amount>=currcoin
        subtract the total amount with the currcoin
    if remaining_amount < currcoin:
        go to next coin 

'''

def coinChange(total_amount,coins):
    remaining_amount = total_amount
    coins.sort(reverse = True)
    i = 0
    while remaining_amount!=0:
        if remaining_amount >= coins[i]:
            remaining_amount = remaining_amount - coins[i]
            print(coins[i])
        if remaining_amount< coins[i]:
            i = i +1



coins = [1,2,5,20,50,100]
coinChange(201, coins)
