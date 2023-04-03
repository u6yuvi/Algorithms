import math

'''
46. Permutations
Permute Array Of Unique Integers
Given an array of unique numbers, return in any order all its permutations.

Example
{
"arr": [1, 2, 3]
}
Output:

[
[1, 2, 3],
[1, 3, 2],
[2, 1, 3],
[2, 3, 1],
[3, 2, 1],
[3, 1, 2]
]

'''

def permute(arr):

    result = []
    slate = []

    def perm_helper(arr,i,slate):
        #base case
        if i==len(arr):
            result.append(slate[:])
            return
        #recursive case
        else:
            for pick in range(i,len(arr)):
                arr[pick], arr[i] = arr[i], arr[pick]
                slate.append(arr[i])
                perm_helper(arr,i+1,slate)
                arr[pick], arr[i] = arr[i], arr[pick]
                slate.pop()
        return
    
    perm_helper(arr,0,slate)
    return result

'''
    
    Time Complexity: Leaf + Intermediate
                     O(n!*n) + <O(n!*n)
                     
    Show that the time taken by the intermediate workers are less than leaf workers:
    No of Leaf Workers - n! 
    Copy the results of size n 
    Time Complexity of Leaf Workers - n!*n
    
    At level 0 ,the number of worker is 1 and worker has 3 choices i.e  Total - n*1 
    At level 1 , the number of worker is n and worker has n-1 choices i.e Tota - n*n-1
    
    
    Space Complexity: Input + Aux + Output
                     O(n)   +  O(n)[Height of the call stack , slate is mutable]   +   O(n!*n)
    
    
    '''

# print(permute([1,2,3]))

#--------------------------------Question-2------------------------------------
'''
784. Letter Case Permutation
Given a string, return all strings that can be generated by changing case of one or more letters in it.

Example One
{
"s": "a1z"
}
Output:

["A1Z", "A1z", "a1Z", "a1z"]

'''
def letter_case_permutations(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    result = []
    slate = []
    
    def letter_helper(s,i,slate):
        #base case
        if i == len(s):
            result.append("".join(slate))
            return 
        #recursive case
        else:
            if s[i].isalpha():
                slate.append(s[i].upper())
                letter_helper(s,i+1,slate)
                slate.pop()
                slate.append(s[i].lower())
                letter_helper(s,i+1,slate)
                slate.pop()
            elif s[i].isdigit():
                slate.append(s[i])
                letter_helper(s,i+1,slate)
                slate.pop()
        return

    letter_helper(s,0,slate)
    return result

'''
Time Complexity : Leaf Node + Intermediate Node
                 O(2^n * n)  + O(2^n*1) -Number of nodes is no more than 2^n when compared with penultimate layer
Space Complexity : Input + Aux Space + Output
                  O(n)   + O(n) + O(2^n*n)
                    
                    
                    '''
# print(letter_case_permutations("a1z"))


#--------------------------Question-3-----------------------
'''
78. Subsets
Generate All Subsets Of A Set
Generate ALL possible subsets of a given set. The set is given in the form of a string s containing distinct lowercase characters 'a' - 'z'.

Example
{
"s": "xy"
}
Output:

["", "x", "y", "xy"]

'''


def generate_all_subsets(s):
    """
    Args:
    s(str)
    Returns:
    list_str
    """
    # Write your code here.

    slate = []
    result = []

    def generate_all_subset_helper(s,i,slate):
        #base case
        if i == len(s):
            result.append("".join(slate))
            return
        
        #recursive case
        else:
            #exclude case
            generate_all_subset_helper(s,i+1,slate)

            #include
            slate.append(s[i])
            generate_all_subset_helper(s,i+1,slate)
            slate.pop()

        return
    
    generate_all_subset_helper(s,0,slate)

    return result
'''
Time Complexity - Leaf Node + Intermediate Node
                2^n * n   + < 2^n*1
Space Complexity - Input + Aux + Output
                    O(n) + O(n) + O(2^n*n)
'''

# print("Generate all subset:",generate_all_subsets("xy"))



#------------------------Question-4--------------------------------------

'''
47. Permutations II
Permute Array Of Integers Duplicates Allowed
Given an array of numbers with possible duplicates, return all of its permutations in any order.

Example
{
"arr": [1, 2, 2]
}
Output:

[
[1, 2, 2],
[2, 1, 2],
[2, 2, 1]
]

'''


def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.

    slate = []
    result = []
    
    def get_permut_helper(arr,i,slate):
        #base case
        if i==len(arr):
            result.append(slate[:])
            return
        #recursion case
        else:
            hmap = {}
            for pick in range(i,len(arr)):
                if arr[pick] not in hmap.keys():
                    hmap[arr[pick]] = 1
                    arr[pick], arr[i] = arr[i], arr[pick]
                    slate.append(arr[i])
                    get_permut_helper(arr,i+1,slate)
                    slate.pop()
                    arr[pick], arr[i] = arr[i], arr[pick]

    
    get_permut_helper(arr,0,slate)
    return result

'''
Worst Case is when all numbers are unique.....
    Time Complexity: Leaf + Intermediate
                     O(n!*n) + <O(n!*n)
                     
    Show that the time taken by the intermediate workers are less than leaf workers:
    No of Leaf Workers - n! 
    Copy the results of size n 
    Time Complexity of Leaf Workers - n!*n
    
    At level 0 ,the number of worker is 1 and worker has 3 choices i.e  Total - n*1 
    At level 1 , the number of worker is n and worker has n-1 choices i.e Tota - n*n-1
    
    
    Space Complexity: Input + Aux + Output
                     O(n)   +  O(n)[Height of the call stack , slate is mutable]   +   O(n!*n)
    
    
    '''
# print(get_permutations([1, 2, 2]))


#-------------------------Question-5-----------------------------------

'''
90. Subsets II
Subsets With Duplicate Characters
Given a string that might contain duplicate characters, find all the possible distinct subsets of that string.

Example One
{
"s": "aab"
}
Output:

["", "a", "aa", "aab", "ab", "b"]

'''
def get_distinct_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.

    slate = []
    result = []
    s = sorted(s)
    def get_distinct_helper(arr,i,slate):
        #base case
        if i==len(arr):
            result.append("".join(slate))
            return

        # recursive case
        else:
            cnt = 0
            cnt = sum([1 for j in s[i:] if j==s[i]])
            #exclude case
            get_distinct_helper(arr,i+cnt,slate)

            #include case
            for pick in range(1,cnt+1):
                slate.append(s[i])
                get_distinct_helper(arr,i+cnt,slate)
            for pick in range(1,cnt+1):
                slate.pop()


    get_distinct_helper(s,0,slate)
    return result

'''
Time Complexity - Leaf Node + Intermediate Node + Other
                O(2^n*n)     +  O(2^n*n) [ Due to cnt]  + Sorting [nlog(n)]
Space Complexity - Input  + Aux + Output
                   O(n)   + O(n)  + O(2^n *n)
'''

# print(get_distinct_subsets("aab"))


#-----------------Question-6---------------------------

'''
Given a seven-digit phone number, return all the character combinations 
that can be generated according to the following mapping:

{
"phone_number": "1234567"
}
Output:

[
"adgjmp",
"adgjmq",
"adgjmr",
"adgjms",
"adgjnp",
...
"cfilns",
"cfilop",
"cfiloq",
"cfilor",
"cfilos"
]
First string "adgjmp" in the first line comes from the first characters mapped 
to digits 2, 3, 4, 5, 6 and 7 respectively. Since digit 1 maps to nothing, nothing 
is appended before 'a'. Similarly, the fifth string "adgjnp" generated from first 
characters of 2, 3, 4, 5 second character of 6 and first character of 7. 
All combinations generated in such a way must be returned in the lexicographical order.
'''


def get_words_from_phone_number(phone_number):
    """
    Args:
     phone_number(str)
    Returns:
     list_str
    """
    # Write your code here.
    hash_map = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],
        "7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}

    slate = []
    result = []
    
    def get_words_helper(phone_number,i,slate):
        #base case
        if i==len(phone_number):
            result.append("".join(slate))
            return
        #recursive case
        elif (phone_number[i]!="1") and (phone_number[i]!="0"):
            for pick in hash_map[str(phone_number[i])]:
                slate.append(pick)
                get_words_helper(phone_number,i+1,slate)
                slate.pop()
        else:
            get_words_helper(phone_number,i+1,slate)    
        return

    get_words_helper(phone_number,0,slate)
    return result

'''
    Time Complexity - Leaf Node + Intermediary Node
                      O(4^n *n)  +  <O(4^n)
    Space Complexity - Input + Aux Space + Output
                       O(n).  + O(n). + O(4^n * n)
'''

# print(get_words_from_phone_number("1234567"))

#-----------------------Question-7--------------------

'''
77. Combinations
N Choose K Combinations
Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.

Example One
{
"n": 5,
"k": 2
}
Output:

[
[1, 2],
[1, 3],
[1, 4],
[1, 5],
[2, 3],
[2, 4],
[2, 5],
[3, 4],
[3, 5],
[4, 5]
]
'''



def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.

    slate = []
    result = []

    def find_combinations_helper(s,i,slate,k):
        
        #backtracking case
        if len(slate)==k:
            result.append(slate[:])
            return
        
        #redundant code in this case as the step size of slate it increasing by 1 so upper condition will be met first.
        if len(slate)>k:
            return 

        # if len(slate)<k:

        #base case
        if i == len(s):
            #result.append("".join(slate))
            return
        
        #recursive case
        else:
            #exclude case
            find_combinations_helper(s,i+1,slate,k)

            #include
            slate.append(s[i])
            find_combinations_helper(s,i+1,slate,k)
            slate.pop()

        return
    
    s = list(range(1,n+1))
    find_combinations_helper(s,0,slate,k)
    return result

# print(find_combinations(5,2))


#--------------------------Question-8------------------------------xxxxxxxxx Not yet solved

'''
Generate All Combinations With Sum Equal To Target
Given an integer array, generate all the unique combinations of the array numbers that sum up to a given target value.

Example One
{
"arr": [1, 2, 3],
"target": 3
}
Output:

[
[3],
[1, 2]
]
'''


def generate_all_combinations(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.

    result = []
    slate = []
    arr = sorted(arr)

    def generate_all_cands_helper(arr,i,slate,target):
        
        #backtracking case
        if len(slate)>0:
            if sum(slate[:])==target:
                result.append(slate[:])
                return
        
       
        if sum(slate)>target:
            return

       
        #base case 
        if i >=len(arr):
            #result.append(slate[:])
            return
        
        #recursion
        else:
            #cnt = 0
            cnt = len([j for j in arr if arr[i]==j])

            #inclusion
            for pick in range(1,cnt+1):
                slate.append(arr[i])
                generate_all_cands_helper(arr,i+cnt,slate,target)
            for pick in range(1,cnt+1):
                slate.pop()

            #exclusion
            generate_all_cands_helper(arr,i+cnt,slate,target)
        return

    generate_all_cands_helper(arr,0,slate,target)
    return result

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# print(sum(arr))
# print(generate_all_combinations(arr,300))



#-----------------------------Question-9--------------------------------------------
def generate_all_valid_parenthesis(n):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.

    slate = []
    result = []

    def parenthesis_helper(n_left,n_right,slate):

        #backtracking case

        if n_left>n_right:
            return
        
        
        #base case
        if n_left==0 and n_right==0:
            result.append("".join(slate))
            return

        #recursive case
        else:
            if n_left>0:
                slate.append("(")
                parenthesis_helper(n_left=n_left-1, n_right=n_right,slate = slate)
                slate.pop()

            if n_right>0:
                slate.append(")")
                parenthesis_helper(n_left,n_right-1,slate)
                slate.pop()

        return
    
    parenthesis_helper(n,n,slate)
    return result

'''
Time Complexity - Leaf Node + Intermediate Node
                O(2^2n) * 2n  + < O(2^2n) * 2n
This is a loose upper bound,we can have a tighter bound as the number of leaf nodes follows Catalan Sequence

Space Complexity - Input + Aux + Output
                   O(2n) + O(2n) + O(2*2n)*2n

'''
# print(generate_all_valid_parenthesis(n=2))


#--------------------------Question-10----------------------------------------

'''
Problem
  
N Queen Problem
Given an integer n, find all possible ways to position n queens on an n×n chessboard so that no two queens attack each other. A queen in chess can move horizontally, vertically, or diagonally.

Do solve the problem using recursion first even if you see some non-recursive approaches.

Example One
{
"n": 4
}
Output:

[
["--q-",
 "q---",
 "---q",
 "-q--"],

["-q--",
 "---q",
 "q---",
 "--q-"]
]
'''

def find_all_arrangements(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_str
    """
    # Write your code here.

    slate = []
    result = []

    def find_all_helper(i,slate):
        #backtracking case
        lastq = len(slate)-1

        #Case-1 Check for same columns
        for earlier_q in range(0,lastq):
            if slate[earlier_q] == slate[lastq]:
                return
        #Case-2
            rowdiff = abs(lastq-earlier_q)
            coldiff = abs(slate[lastq] - slate[earlier_q])
            if rowdiff==coldiff:
                return

        #base case
        if i==n:
            result.append(slate[:])
            return

        #recusion
        else:
            for col in range(0,n):
                slate.append(col)
                find_all_helper(i+1,slate)
                slate.pop()
        return

    find_all_helper(0,slate)
    return result

# print(len(find_all_arrangements(n=8)))

#------------------------------Question-11-------------------
'''
131. Palindrome Partitioning
Palindromic Decomposition Of A String
Find all palindromic decompositions of a given string s.

A palindromic decomposition of string is a decomposition of the string into substrings, such that all those substrings are valid palindromes.

Example
{
"s": "abracadabra"
}
Output:

["a|b|r|a|c|ada|b|r|a", "a|b|r|aca|d|a|b|r|a", "a|b|r|a|c|a|d|a|b|r|a"]
'''

def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.

    slate = []
    result = []
    def generate_palindromic(s,i,slate):

        #backtracing case

        def check_palindrome(s):
            # if s!= s[::-1]:
            #     return False
            # return True
        
            mid = len(s)//2
            for k in range(0,mid+1):
                if s[k] != s[len(s)-k-1]:
                    return False
            return True

        if len(slate)>0 and not check_palindrome(slate[-1]):
                return 
        #base case
        if i ==len(s):
            result.append("|".join(slate))

        #recursive case
        else:
            for pick in range(i,len(s)):
                slate.append(s[i:pick+1])
                generate_palindromic(s,pick+1,slate)
                slate.pop()

        return
    
    generate_palindromic(s,0,slate)
    return result

# print(generate_palindromic_decompositions("aab"))


#--------------------------Timed Test--------------------------------------------
#Question-1

'''
Possible To Achieve Target Sum
Given a set of integers and a target value k, find whether there is a non-empty subset that sums up to k.

Example One
{
"arr": [2, 4, 8],
"k": 6
}
Output:

1
Because 2 + 4 = 6.

'''

#Solution - Because it is asking for if any subset equals to target return True or False,we donot need to check for duplicates
#Handle duplicates only when it is asked to generate all subsets that sums to target

def check_if_sum_possible(arr, k):
    """
    Args:
     arr(list_int64)
     k(int64)
    Returns:
     bool
    """
    # Write your code here.
    
    
    slate = []
    result = []
    arr = sorted(arr)
    
    def check_if_helper(arr,i,slate):



        #backtracing case
        if len(slate)>0:
            if sum(slate[:]) == k:
                result.append(slate[:])
                return
        
        #base case
        if i >=len(arr):
            #result.append(sum(slate[:]))
            return
        
        else:

            #include
            cnt = 0
            cnt = len([j for j in arr if j == arr[i]])
            
            for pick in range(1,cnt+1):
                slate.append(arr[i])
                check_if_helper(arr,i+cnt,slate)
                
            for pick in range(1,cnt+1):
                slate.pop()

            #exclude case
            check_if_helper(arr,i+1,slate)
            
        return
    
    
    check_if_helper(arr,0,slate)
        #recursion case
    if result:
        return result
    return False

# print(check_if_sum_possible([-4, -3, -1, 3, -3, -2, -1, -3, 4, -2, -3, -4, -4, -2, -1, 4, 3, -1],k=15))


#Question-2
'''
22. Generate Parentheses
'''
def find_all_well_formed_brackets(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    # Write your code here.
    
    slate = []
    nleft = n
    nright=n
    result = []
    
    def find_all_well_helper(nleft,nright,slate):
        
        #backtracking case
        
        if nleft>nright:
            return
        
        #base case
        if nleft==0 and nright==0:
            result.append("".join(slate))
            return
        
        
        
        #recrusive case
        else:
            if nleft>0:
                slate.append("(")
                find_all_well_helper(nleft-1,nright,slate)
                slate.pop()
            if nright>0:
                slate.append(")")
                find_all_well_helper(nleft,nright-1,slate)
                slate.pop()
        return
    
    find_all_well_helper(nleft,nright,slate)
    return result

# print(find_all_well_formed_brackets(3))

#TODO:
'''
1. Solve each problem as a Decision Problem ,Yes or No
2. Solve each problem as a Count problem.

'''



def distinctNames(ideas) -> int:
        
    slate = []
    result = [0]
    def sol_helper(ideas,i,slate):
        if len(slate)==2:
            a,b = slate[0][0] , slate[1][0]
            str1 = a +"".join(slate[1][1:])
            str2 = b + "".join(slate[0][1:])
            if str1 not in ideas and str2 not in ideas:
                result[0] = result[0]+1
                
        else:
            for pick in range(i,len(ideas)):
                ideas[i],ideas[pick] = ideas[pick], ideas[i]
                slate.append(ideas[i])
                sol_helper(ideas,i+1,slate)
                slate.pop()
                ideas[i],ideas[pick] = ideas[pick], ideas[i]
        
    
    sol_helper(ideas,0,slate)
    return result[0]
        

print(distinctNames(["coffee","donuts","time","toffee"]))



#---------------Problem---------------------
'''
39. Combination Sum
'''

def combinationSum(candidates: int, target: int):
    
        '''Assumption 
        All the numbers in the array are positive
        if they are negative , backtracking case - sum(slate[:])>target is not the correct condition as there could be negative numbers afterwards.
        Soln- Sort the numbers and then do the same
        '''
        #Naive Way
        #         slate = []
        #         result = []
                
        #         def helper(arr,i,slate):
        #             #print(slate,target,result)
                    
        #             #backtrack case
        #             if sum(slate[:])==target:
        #                 result.append(slate[:])
        #                 return
                    
        #             #backtrack 
        #             if sum(slate[:]) >target:
        #                 return
        #             #base
        #             if i ==len(arr):
        #                 return 
                
                        
        #             #recursive cas
                    
        #             #include
        #             cnt = 1
        #             cnt = math.floor(target/arr[i])
        #             cnt = max(cnt,1)
        #             for pick in range(1,cnt+1):
        #                 slate.append(arr[i])
        #                 helper(arr,i+1,slate)
                    
        #             for pick in range(1,cnt+1):
        #                 slate.pop()
        #             #exclude 
        #             helper(arr,i+1,slate)
                    
        #         helper(candidates,0,slate)
        #         return result
            
        #Optimised Version
        '''
        Keep the running sum so that leaf worker need not recalculate it
        '''


        slate = []
        result = []
        
        def helper(arr,i,slate,running_sum):
            #print(slate,target,result)
            
            #backtrack case
            if running_sum==target:
                result.append(slate[:])
                return
            
            #backtrack 
            if running_sum >target:
                return
            #base
            if i ==len(arr):
                return 
        
                
            #recursive cas
            
            #include
            cnt = 1
            cnt = math.floor(target/arr[i])
            cnt = max(cnt,1)
            for pick in range(1,cnt+1):
                slate.append(arr[i])
                helper(arr,i+1,slate,running_sum+arr[i]*pick)
            
            for pick in range(1,cnt+1):
                slate.pop()
            #exclude 
            helper(arr,i+1,slate,running_sum)
            
        helper(candidates,0,slate,0)
        return result


        '''
        Time Complexity - Intermediate Node + Leaf Node
            Number of workers[(2^t1)*2(t2)..2^(tn)] * Work done per worker(O(1)) + \
            
            Leaf Node -[(2^t1)*2(t2)..2^(tn)]* Size of the array O(n)
            
        Space Complexity - Input [O(n)] + Aux[O(n)] + Leaf [[(2^t1)*2(t2)..2^(tn)]*n]

        https://leetcode.com/problems/combination-sum/discuss/1755084/Detailed-Time-and-Space-Complexity-analysisc%2B%2Bjavabacktracking
        '''
print(combinationSum([2,3,6,7],7))


#----------------------------Problem----------------------------------------
'''
40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''
def combinationSum2(candidates, target):
        
        
    result = []
    slate = []
    arr = sorted(candidates)
    
    def helper(arr,i,slate,running_sum):
        
        #backtrack
        if running_sum == target:
            result.append(slate[:])
            return
        if running_sum >target:
            return
        
        if i >=len(arr):
            return
        
        #recursive case
        

        
        #include
        
        cnt = len([j for j in arr[i:] if j ==arr[i] ])
        for pick in range(1,cnt+1):
            slate.append(arr[i])
            helper(arr,i+cnt,slate,running_sum+arr[i]*pick)
            
        for pick in range(1,cnt+1):
            slate.pop()
        #exclude
        helper(arr,i+cnt,slate,running_sum)
            
    
    helper(arr,0,slate,0)
    return result

print(combinationSum2([10,1,2,7,6,1,5],8))    




        
def test(s):
        
        result = []
        slate = []
        
        def helper(arr,i,slate):
            
            #check if newly added substring in slate is a pallindrome
            
            def checkpallin(s):
                mid = len(s)//2
                for k in range(0,mid+1):
                    if s[k]!= s[len(s)-k-1]:
                        return False
                return True
            #backtrack
            if len(slate)>0 and not checkpallin(slate[-1]):
                return
                
            
            #base case
            if i==len(arr):
                result.append(slate[:])
                return
            
            #recursive case
            
            for pick in range(i,len(arr)):
                slate.append(arr[i:pick+1])
                helper(arr,pick+1,slate)
                slate.pop()
        
        
        helper(s,0,slate)
        return result

print(test("aab"))
                    