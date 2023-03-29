'''
706. Design HashMap
'''

class MyHashMap:

    def __init__(self):
        self.num_bucket = 1000
        self.bucket = [-1]*self.num_bucket
        
    def put(self, key: int, value: int) -> None:
        
        idx = key % self.num_bucket
        # if nothing at hash index
        if self.bucket[idx] ==-1:
            self.bucket[idx] = [[key,value]]
            return 
        # if earlier value present at the same hash_index and key
        for pos, kv  in enumerate(self.bucket[idx]):
            if kv[0] == key:
                self.bucket[idx][pos][1] = value
                return 
        #if hash_index exists but no key
        self.bucket[idx].append([key,value])
        return
        

    def get(self, key: int) -> int:
        
        idx = key%self.num_bucket
        #if key doesnot exist
        if self.bucket[idx]==-1:
            return -1
        #if key exisits
        for pos , kv in enumerate(self.bucket[idx]):
            if kv[0]==key:
                return kv[1]
        return -1
        
        

    def remove(self, key: int) -> None:
        
        idx = key%self.num_bucket
        # if no data
        if self.bucket[idx]==-1:
            return
        # if key exisits
        for pos, kv in enumerate(self.bucket[idx]):
            if kv[0]==key:
                del self.bucket[idx][pos]
                
        return
            

'''
1961. Check If String Is a Prefix of Array
'''
def isPrefixString(s: str, words) -> bool:
    
    i = 0
    for word in words:
        if s[i:i+len(word)] != word:
            return False
        else:
            i+=len(word)
        if i==len(s):
            return True


'''
155. Min Stack
'''

class MinStack:

    def __init__(self):
        self.size = 0
        self.min = []
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.size ==0:
            self.min.append(val)
        else:
            self.min.append(self.short(val,self.min[self.size-1]))
        self.stack.append(val)
        self.size+=1
        

    def pop(self) -> None:
        del self.min[self.size-1]
        del self.stack[self.size-1]
        self.size-=1
        

    def top(self) -> int:
        return self.stack[self.size-1]
        

    def getMin(self) -> int:
        return self.min[self.size-1]
        
    def short(self,a,b):
        if a<b:
            return a
        return b
        