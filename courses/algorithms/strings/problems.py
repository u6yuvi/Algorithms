#---------------------Problem--------------------------

'''
151. Reverse Words in a String
'''

def reverseWords( s: str) -> str:
    
    s1 = s.split(" ")

    i = 0
    j = len(s1)-1

    while i<=j:
        s1[i], s1[j] = s1[j], s1[i]
        i+=1
        j-=1
    
    return " ".join([i for i in s1 if i!=''])

print(reverseWords("  hello world  "))

#---------------------Problem--------------------------
'''
14. Longest Common Prefix
'''
def longestCommonPrefix( strs) -> str:
    
    '''https://www.geeksforgeeks.org/longest-common-prefix-using-sorting/
    '''
    # Word by Word Comparision
    sorted_strs  = sorted(strs)
    
    #mind length
    end = min(len(sorted_strs[-1]) ,len(sorted_strs[0]))
    i = 0
    while i <end and sorted_strs[0][i]==sorted_strs[-1][i]:
        i+=1
    
    prefix = sorted_strs[0][0:i]
    return prefix


#---------------------Problem--------------------------
'''
205. Isomorphic Strings
'''

def isIsomorphic( s: str, t: str) -> bool:
    
    hmap1 = {}
    hmap2 = {}
    for i,j in zip(s,t):
        if i not in hmap1 and j not in hmap2:
            hmap1[i] = j
            hmap2[j] = i
        elif hmap1.get(i)!=j and hmap2.get(j)!=i:
            return False
    return True


#---------------------Problem--------------------------
'''
Prem- 243. Shortest Word Distance
'''
'''
Closest Strings
Given a list of words followed by two words, the task to \
    find the minimum distance between the given two words in the list of words
'''

'''
Input:
S = { "the", "quick", "brown", "fox", 
     "quick"}
word1 = "the"
word2 = "fox"
Output: 3
Explanation: Minimum distance between the 
words "the" and "fox" is 3
'''
'''
Input:
S = {"geeks", "for", "geeks", "contribute", 
     "practice"}
word1 = "geeks"
word2 = "practice"
Output: 2
Explanation: Minimum distance between the
words "geeks" and "practice" is 2
'''

def closest_string(arr,s1,s2):
    d1 = []
    d2 = []
    for i ,j in enumerate(arr):
        if j == s1:
            d1.append(i)

        if j == s2:
            d2.append(i)

    return d2[0]-d1[0]

print("Closest String ",closest_string(["the", "quick", "brown", "fox", 
     "quick"],"the","fox"))   

#---------------------Problem--------------------------
'''
242. Valid Anagram
'''

def isAnagram( s: str, t: str) -> bool:
    
    
    hmap = {}
    for i in s:
        if i in hmap:
            hmap[i]+=1
        else:
            hmap[i] = 1
            
    for j in t:
        if j in hmap:
            hmap[j]-=1
            if hmap[j]==0:
                del hmap[j]
        else:
            return False
        
    if hmap:
        return False
    return True    


'''
1347. Minimum Number of Steps to Make Two Strings Anagram
'''

def minSteps( s: str, t: str) -> int:
    cnt = 0
    hmap = {}
    for i in s:
        if i in hmap:
            hmap[i]+=1
        else:
            hmap[i] = 1

    for j in t:
        if j in hmap:
            hmap[j]-=1
            if hmap[j]==0:
                del hmap[j]
        else:
            cnt+=1

    return cnt

#----------------------Problem--------------------
'''
1832. Check if the Sentence Is Pangram
'''

def checkIfPangram(sentence: str) -> bool:
    
    mask = []
    for i in range(26):
        mask.append(0)
        
    for i in sentence:
        mask[ord(i.lower()) - ord("a")] = 1
        
    if sum(mask)==26:
        return True
    return False


'''
49. Group Anagrams
'''

def groupAnagrams(strs):
    
    '''
    Time Complexity = O(m*n)
    m- No of words
    n = avg length of words
    '''
    hashmap = {}
    for word in strs:
        mask = [0]*26
        
        for c in word:
            mask[ord(c)-ord("a")]+=1
            
        if tuple(mask) in hashmap:
            hashmap[tuple(mask)].append(word)
        else:
            hashmap[tuple(mask)] = [word]
        
    return list(hashmap.values())


'''
125. Valid Palindrome
'''

#Approach -1  - Additional Space O(n)
def isPalindrome( s: str) -> bool:
    news = []
    for i in s:
        if i.isalnum():
            news.append(i.lower())
            
    if len(news)>0:
        if len(news)%2!=0:
            mid = len(news)//2 +1
        else:
            mid = len(news)//2

        for i in range(0,mid):
            if news[i]!=news[len(news)-i-1]:
                return False

        return True
    return True
    

#Approach -2 Two pointer

def isPalindrome(s: str) -> bool:
    
    i = 0
    j = len(s)-1
    flag = True
    while i<j:
        if s[i].isalnum() and s[j].isalnum():
                if s[i].lower()!=s[j].lower():
                    flag = False
                    break
                i+=1
                j-=1
        else:
            if not s[i].isalnum():
                i+=1
            if not s[j].isalnum():
                j-=1

    return flag

'''
647. Palindromic Substrings

'''
def countSubstrings(s: str) -> int:
    cnt =0
    for idxi,i in enumerate(s):
        for idxj, j in enumerate(s[idxi:],idxi):
            #print(s[idxi:idxj+1])
            if s[idxi] == s[idxj] and s[idxi:idxj+1] == s[idxi:idxj+1][::-1]:
                cnt+=1
    return cnt
            