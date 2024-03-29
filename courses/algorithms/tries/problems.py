from typing import List

'''
208. Implement Trie (Prefix Tree)
'''


class TrieNode:
    def __init__(self,b = False):
        self.end = b
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode(False)

    def insert(self, word: str) -> None:
        
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode(False)
            curr = curr.children[word[i]]
        curr.end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] not in curr.children:
                return False
            curr = curr.children[prefix[i]]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


'''
1804. Implement Trie (Prefix Tree)
Implement the following 
1. Count Wordsequal to
2. Count words starting with 
3. Erase word

'''

class TrieNode:
    def __init__(self,b = 0):
        self.end = b # instead of Boolean flag it will be used to count
        self.total = 0
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode(0)

    def insert(self, word: str) -> None:
        
        curr = self.root
        for i in range(len(word)):
            curr.total+=1
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode(0)
            curr = curr.children[word[i]]
        curr.end +=1
        

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        
        return curr.end
        
    def countwordsequalto(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                return 0
            curr = curr.children[word[i]]
        
        return curr.end

    def countwordsstartingwith(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                return 0
            curr = curr.children[word[i]]
        
        return curr.total

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] not in curr.children:
                return False
            curr = curr.children[prefix[i]]
        
        return True

    def erase(self,word):
        curr = self.root

        for i in range(len(word)):
            curr.total-=1
            if curr.children[word[i]].total==1:
                del curr.children[word[i]]
                return
            curr = curr.children[word[i]]
        curr.end-=1
        curr.total-=1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


'''
720. Longest Word in Dictionary
'''
def longestWord(self, words: List[str]) -> str:
    
#Implement Tries

    class TrieNode():
        def __init__(self,):
            self.end = False
            self.children = {}

    root = TrieNode()
    root.end = True

    #Implement Tries
    for word in words:
        curr = root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]] 

        curr.end = True

    #traversal
    slate = []
    self.result = [""]

    def helper(curr, slate):
        #backtrackcase
        if curr.end is False:
            return

        #base and recursive case
        if len(slate) > len(self.result[0]) or\
        len(slate)== len(self.result[0]) and "".join(slate[:]) < self.result[0]:
            self.result[0] = "".join(slate[:])

        for child in curr.children:
            slate.append(child)
            helper(curr.children[child],slate)
            slate.pop()
    helper(root,slate)
    return self.result[0]