# Creating Tuple

a = 2,3,4,5 # tuple
a = (2,3,4,5) # tuple
a = ('2') # string
a = ('2',) #tuple
a = tuple('2345') # tuple(2,3,4,5) 
a = tuple([2,3,4,5])
print(a)

# Time Complexity of creating tuple O(1)
# Space Complexity of creating tuple O(n)

# Memory Management 
'''
Like lists and arrays, it is stoed in contiguos block of memory.
Immutable -Once declared cannot be changed.
'''
#Access elements in tuple

print(a[1:3])

#Traversing tuple

for i in a:
    print(a)

for i in range(len(a)):
    print(a[i])

#Time Complexity - O(n)
# Space Complexity - O(1)

#Find element in a tuple

if 2 in a:
    print(True)
for i in a:
    if i ==3:
        print(a.index(i))

#tuple operations
b = (4,5,6)
print(a+b) # new tuple with values concatenated

#repetitions
print(a *4) # new tuple with each elements repeated 4 times

#count occurances
print(a.count(2))

len(a)
a.index(2)
max(a)
min(a)
tuple([1,2,3,4]) # list to tuple

#cannot change an element from tuple but can reassign
#a[2] =3 # error
a = 4,5,6,7

#del a[2] # error
del a # delete the entire tuple

#Methods not available in tuple
# append, insert,remove,pop,clear,sort,reverse 

#when to use
'''
1. use tuple for heterogous datatypes whereas list for homogenous
2. iterating in a tuple is faster than list ???
3. tuple that contains immutable elments can be converted in a key of dicitionary
4. Implement tupe for data which is not going to change to guarantee that it
remains write protected.
'''