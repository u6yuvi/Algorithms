'''
5. Longest Palindromic Substring
'''

def longestPalindrome(s: str) -> str:
    
    #Brute Force
    sub = ""
    for idx, char in enumerate(s):
        for idxj , charj in enumerate(s[idx:],idx):
            if char == charj and s[idx:idxj+1]==s[idx:idxj+1][::-1] \
            and len(s[idx:idxj+1])>len(sub):
                sub = s[idx:idxj+1]
                
    return sub
        