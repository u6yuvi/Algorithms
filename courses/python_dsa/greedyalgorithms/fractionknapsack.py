'''
Fractional Knapsack Problem
Given a set of items, each with a weight and a value,
 determine the number of each item to include in a collection so 
 that the total weight is less than or equal to a given limit and the 
 total value is as large as possible.
'''



class Item:
    def __init__(self,w,v):
        self.weight = w
        self.value = v
        self.density = self.value/self.weight

def knapsackMethod(clist,capacity):
    clist.sort(key = lambda x: x.density,reverse = True)
    remaining_capacity = capacity
    i = 0
    boxes = []
    while remaining_capacity!=0:
        if remaining_capacity>= clist[i].weight:
            remaining_capacity -= clist[i].weight
            boxes.append(clist[i].weight)
        elif remaining_capacity <clist[i].weight:
            frac = remaining_capacity/clist[i].weight
            remaining_capacity = remaining_capacity -clist[i].weight*frac
            boxes.append(clist[i].weight) 
        i = i+1
    return boxes





item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
cList = [item1, item2, item3]

assert knapsackMethod(cList, 50) == [10,20,30] , "Passed"