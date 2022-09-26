#Recursion
#Single branching - O(n)
#Multiple Branching with b branches  and d depth = branches^depth 
#Time Complexity - 2^n
# Space Complexity - O(n)
'''
Step-1 : Identify recursive case - the flow
n! = n* (n-1)!

Step2: Base Case - the stopping criteria
if n =0 or 1 

Step3: Unintentional case - the constraint

n is a positive integer
'''

def factorial(n):
    if n>0 and int(n) == n: # unintended case - constrains
        if n in [0,1]: # base condition
            return 1
        else:
            return n * factorial(n-1) # recursion case

def fibonaci(n):
    '''
    Each number is the sum of preceeding two numbers and the sequence starts from 0 and 1
    Fibbo(n) = 0 ,1,1,2,3,5,8,13
    
    1. Recursive case
    Fibbo(n) = Fibbo(n-1) + Fibbo(n-2)
    
    2. Base Case 
    if n=1 or 0 , return n

    3. Unintensional case
    n is a positive integer
    '''
    if n>=0 and int(n)==n:

        if n in [0,1]:
            return n
        else:
            return fibonaci(n-1) + fibonaci(n-2) # recursive case

#Sum of digits of positive integer number using recursion
'''
if n = 232
F(n) = 2+3+2 
'''
def sum_digits(n):
    '''
    Step 1: Recursion case 
    n%2
    Step 2: base case
    if n<10 return n

    Step3: Unitentional case
    n is a positive integer
    '''
    #print(n)
    
    if n>=0 and int(n) ==n:
        if n ==0:
            return 0
        else:
            remainder = n%10
            new_n = int(n/10)
            return remainder + sum_digits(new_n)

# Calculate Power of a number using recursion

def pow(x,n):
    '''
    Step 1 : Recursion case
    F( x^n) = x * x * x ... n times
    x^n = x * x^n-1

    Step 2: Base case 
    if n==0 , return 1
    if n==1 , return x
    
    Step3:
    n is a positive integer
    '''
    if x>=0 and int(x)==x :
        if n==0:
            return 1
        if n==1:
            return x
        else:
            return x*pow(x,n-1)

#Greatest Common Divisor
'''
Eg: 48,18  
Divide 48/12 and get remainder (r) and quotient (q)
then divide 12/q and continue till remainder is 0 .if remainder is 0 , the q element will be the answer'''
def gcd(a,b):
    '''
    Step1: Recursion case - gcd(a,a%b)

    Step 2: Base case - gcd(a,0) = 0

    Step 3: Constrains
        a !=0 and int
    '''
    if a!=0 and int(a) == a and b!=0 and int(b) ==b:
        if a<0:
            a = -1*a
        if b<0:
            b = -1*b
    
    if b ==0:
        return a
    else:
        return gcd(b,a%b)

def decimal_to_binary(a):
    '''
    13/2 = 6,1
    6/2 = 3, 0
    3/2 = 1,1
    1/2 = 0,1'''

    if int(a) == a:
        if a==0:
            return 0
        return a%2 + 10*  decimal_to_binary(a//2)


def product_of_arrays(arr):
    '''
    array = [1,2,3,4] = 24'''
    if arr:
        if len(arr)==1:
            return arr[0]
        return arr[-1] * product_of_arrays(arr[:-1])


def isPalindrome(strng):
    if len(strng)==0:
        return True
    if strng[0]!=strng[-1]:
        return False

    return isPalindrome(strng[1:-1])


'''
Write a recursive function called someRecursive which accepts an array 
and a callback. The function returns true if a single value in the array 
returns true when passed to the callback. Otherwise it returns false.

Examples

someRecursive([1,2,3,4], isOdd) # true
someRecursive([4,6,8,9], isOdd) # true
someRecursive([4,6,8], isOdd) # false

'''

def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
    if len(arr) ==0 :
        return False
    if not cb(arr[0]):
        return someRecursive(arr[1:],cb)
    
    return True


def flatten(arr):
    
    resultarr = []

    for item in arr:
        if isinstance(item,list):
            resultarr.extend(flatten(item))
        else:
            resultarr.append(item)
    return resultarr

'''
Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.

Example

capitalizeFirst(['car', 'taco', 'banana']) # ['Car','Taco','Banana']

'''
def capitalzeFirst(arr):

    '''
    Recursiver condition - F(arr) =  arr[0].upper + F(arr[1:])
    '''
    result = []
    if len(arr)==0:
        return result
    result.append(arr[0].capitalize())
    return result + capitalzeFirst(arr[1:])

'''
Write a recursive function called nestedEvenSum. Return the sum of all even numbers in an object which may contain nested objects.

Examples

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}
 
obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}
 
nestedEvenSum(obj1) # 6
nestedEvenSum(obj2) # 10
  

'''
def nestedEvenSum(arr):
#Recursive condition -   

    sum1 = 0
    for key in arr:
        #print(key)
        if type(arr[key])==dict:
            #print("rec",key)
            sum1+= nestedEvenSum(arr[key])
        elif isinstance(arr[key],int)  and arr[key]%2==0:
            sum1 += arr[key]

    return sum1


'''
Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and converts them to strings. Recursion would be a great way to solve this!

Examples

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}
 
stringifyNumbers(obj)
 
{'num': '1', 
 'test': [], 
 'data': {'val': '4', 
          'info': {'isRight': True, 'random': '66'}
          }
}
'''

def stringifyNumbers(obj):    ######bug
    '''
    Recursive condition -  F(obj) =  F(obj[1:]
    '''
    new_dict = obj
    for key in obj:
        if type(obj[key]) is dict:
            new_dict[key] = stringifyNumbers(obj[key])
        if isinstance(obj[key],int):
            new_dict[key] = str(obj[key])
    return new_dict


'''
collectStrings
Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a typeof string.

Examples

obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
 
collectStrings(obj) # ['foo', 'bar', 'baz']
  
'''

def collectStrings(obj):
    result = []
    for key in obj:
        if type(obj[key]) is dict:
            result = result + (collectStrings(obj[key]))

        if type(obj[key]) is str:
            result.append(obj[key])

    return result


def findnummaxrec(arr,n)


if __name__ == "__main__":

    assert factorial(4) ==24

    assert fibonaci(7) == 13

    assert sum_digits(234556789) == 49

    assert pow(2,4) ==16

    assert gcd(48,18) == 6

    assert(decimal_to_binary(13)) == 1101

    assert product_of_arrays([1,2,3,4]) == 24

    assert isPalindrome(["toot"]) == True

    assert someRecursive([2,4,6],isOdd) == False, "Checked" 


    assert flatten([[[1]],2,[3,4]]) == [1,2,3,4]

    assert capitalzeFirst(["abc","def"]) == ["Abc","Def"]

    assert nestedEvenSum({"a":{"b":2,"c":3,"d":4},"m":5}) == 6

    assert nestedEvenSum({
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}) == 10

    input = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
        "isRight": True,
        "random": 66
        }
    }
    }

    expected = {'num': '1', 
    'test': [], 
    'data': {'val': '4', 
            'info': {'isRight': True, 'random': '66'}
            }
    }

    #print(stringifyNumbers(input))
    #assert stringifyNumbers(input) == expected

    input =  {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
    print(collectStrings(input))