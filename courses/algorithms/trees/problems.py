from utils import input_BinaryTreeNode_int32
from utils import BinaryTreeNode
from typing import List

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

def run(data,func,**args):
    root = input_BinaryTreeNode_int32(data["root"])
    print(func(root,**args))
#-------------------Problem-1--------------------------------------------------
'''
102. Binary Tree Level Order Traversal

'''
def level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    '''
    Time Complexity - O(n)
    Space Complexity - Worst Case O(n/2) ~O(n) - Number of nodes in the leaf level
    We know around 50% of nodes are in the last level
    '''
    result = []
    if root is None:
        return result
    queue = [root]
    while queue:
        numnodes = len(queue)
        temp = []
        for i in range(0,numnodes):
            node = queue.pop(0)
            temp.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(temp)
    return result

#----------------------------------Problem-2-----------------------------------------------------
'''
429. N-ary Tree Level Order Traversal
'''

"""
For your reference:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
"""
def level_order(root):
    """
    Args:
     root(TreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []
    if root is None:
        return result
    queue = [root]
    result = []
    while queue:
        numnode = len(queue)
        temp = []
        for i in range(0,numnode):
            node = queue.pop(0)
            temp.append(node.value)
            for child in node.children:
                queue.append(child)
    
        result.append(temp)
    return result


#--------------------Problem-3------------------------------------------------------------
'''
199. Binary Tree Right Side View
'''

def right_view(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    result = []
    if result is None:
        return []
    queue = [root]
    while queue:
        numnodes = len(queue)
        for i in range(0,numnodes):
            node = queue.pop(0)
            temp = node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(temp[-1])
    return result

#---------------------------------Problem-3-----------------------------------------------

'''
107. Binary Tree Level Order Traversal II

Reverse Level Order Traversal
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def reverse_level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []
    if root is None:
        return result
    queue = [root]
    result = []
    while queue:
        numnode = len(queue)
        temp = []
        for i in range(0,numnode):
            node = queue.pop(0)
            temp.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
        result.append(temp)
    #reverse the result
    return result[::-1]


#---------------------------------Problem-4----------------------------------------------
'''
103. Binary Tree Zigzag Level Order Traversal
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def zigzag_level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []
    if root is None:
        return result
    queue = [root]
    righttoleft=False
    while queue:
        numnode = len(queue)
        temp = []
        for i in range(0,numnode):
            node = queue.pop(0)
            temp.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if righttoleft:
            result.append(temp[::-1])
        else:
            result.append(temp)
        righttoleft = not righttoleft
        
    return result


#---------------------------------Problem-5----------------------------------------------
'''
2415. Reverse Odd Levels of Binary Tree

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reverseOddLevels( root):

        if root is None:
            return []
        
        result = []
        q = [root]
        while q:
            q_len = len(q)
            temp = []
            i = 0
            for _ in range(q_len):
                node = q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if i%2==0:
                result.extend(temp)
            else:
                result.extend(temp[::-1])
            i=i+1

        def insertLevelOrder(arr, i, n):
            root = None
            if i < n:
                root = TreeNode(arr[i]) 
                root.left = insertLevelOrder(arr, 2 * i + 1, n)
                root.right = insertLevelOrder(arr, 2 * i + 2, n)

            return root
        root = None
        n = len(result)
        root = insertLevelOrder(result,0,n)
        return root

#-------------------------Problem-5-----------------------------------------

'''
543. Diameter of Binary Tree
Diameter of the Binary Tree
'''


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def binary_tree_diameter(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    if root is None:
        return 0
    global_diam = [0]
    
    def binary_tree_diameter_helper(node):
        #base case
        if node.left is None and node.right is None:
            return 0
            
        #recursive case
        my_diam = 0
        LH = 0
        if node.left:
            LH = binary_tree_diameter_helper(node.left)
            my_diam = my_diam + LH + 1
        if node.right:
            RH = binary_tree_diameter_helper(node.right)
            my_diam = my_diam  + RH +1
            LH = max(LH,RH)
        global_diam[0] = max(my_diam,global_diam[0])
        return LH + 1
    
    binary_tree_diameter_helper(root)
    
    return global_diam[0]

#----------------------------Problem-6-------------------------------------
'''
113. Path Sum II
Print all paths that sum to k 
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def all_paths_sum_k(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     list_list_int32
    """
    '''
    Worst Case Scenario is when it is a balanced binary tree as in that case there \
    could be n/2[number of leaf nodes] such paths with each of size log(n)[height]

    Time Complexity - Leaf Node + Intermediate node
                    O(nlog(n)) + Constant Work
    Space Complexity - Input + Aux + Ouptut
                                O(log(n)) + O(nlog(n))
    '''


    result = []
    slate = []
    if root is None:
        return result
    
    def helper_all_path_sum_k(node,target,slate):
        #base case
        if node.left is None and node.right is None:
            if target==node.value:
                slate.append(node.value)
                result.append(slate[:])
                slate.pop()
            
        #recusive case
        if node.left:
            slate.append(node.value)
            helper_all_path_sum_k(node.left,target-node.value,slate)
            # ensuring to pop in case no right node
            slate.pop()
        if node.right:
            slate.append(node.value)
            helper_all_path_sum_k(node.right,target-node.value,slate)
            slate.pop()
    
            
    helper_all_path_sum_k(root,k,slate)
    
    if not result:
        result.append([-1])
    return result


#---------------------------Problem-7-----------------------------------------

'''
112. Path Sum
Root To Leaf Path Sum Equal To K
'''


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def path_sum(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     bool
    """
    '''
    Time Complexity = No of nodes * Word done per node
                      n * O(1)  = O(n)
    Space Complexity = Height of the binary tree = O(logn)
    '''
    result = [False]
    if root is None:
        return result
    def helper_path_sum(node,target):
        #base case
        if node.left is None and node.right is None:
            if target==node.value:
                result[0] = True
            return 
        
        #recursive case
        if node.left is not None:
            helper_path_sum(node.left,target-node.value)
        if node.right is not None:
            helper_path_sum(node.right,target-node.value)
        
            
    helper_path_sum(root,k)
    if result:
        return result[0]
        

#----------------------------Problem-----------------------------------

'''
250 count-univalue-subtrees/
https://leetcode.com/problems/count-univalue-subtrees/
'''
def count_unival(root):


    global_cnt = [0]
    def count_unival_helper(node):
        if node.left is not None and node.right is not None:
            global_cnt[0] = global_cnt[0]+1
            return True


        #recursive case
        unival = True
        left = True
        right = True
        if node.left:
            left = count_unival_helper(node.left)
            if not left and node.val != node.left.val:
                unival = False
            
        if node.right:
            right = count_unival_helper(node.right)
            if not right and node.val!=node.right.val:
                unival = False
        
        if unival:
            global_cnt[0] = global_cnt[0] +1

        return unival
    
    count_unival_helper(root)
    return global_cnt



#----------------------------Problem-8----------------------------------

'''
Preorder Traversal
'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    result = []
    if root is None:
        return result
    def preorder_helper(node):
        if node.left is None and node.right is None:
            result.append(node.value)
            return 
        #recursive case
        isnode = False
        if node.left is not None:
            result.append(node.value)
            isnode = not isnode
            preorder_helper(node.left)
        if node.right is not None:
            if not isnode:
            #if node.value not in result:
                result.append(node.value)
            preorder_helper(node.right)
    
    
    preorder_helper(root)
    return result

#----------------------------Problem-8.1----------------------------------

'''
Preorder Traversal-Optimised
'''

def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    result = []
    if root is None:
        return result
    def preorder_helper(node):
        #base case
        # if node.left is None and node.right is None:
        #     result.append(node.value)
        #     return 
        #recursive case
        result.append(node.value)
        if node.left is not None:
            preorder_helper(node.left)
            # result.append(node.value)
            # isnode = not isnode
        if node.right is not None:
            preorder_helper(node.right)
    
    
    preorder_helper(root)
    return result

#----------------------------Problem-9----------------------------------

'''
Preorder Traversal-Optimised
'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def inorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    result = []
    if root is None:
        return result
    def inorder_helper(node):
        #base case
        # if node.left is None and node.right is None:
        #     result.append(node.value)
        #     return 
        #recursive case
        if node.left is not None:
            inorder_helper(node.left)
        result.append(node.value)
        if node.right is not None:
            inorder_helper(node.right)
    
    
    inorder_helper(root)
    return result



#----------------------------Problem-10----------------------------------

'''
Postorder Traversal
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def postorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    result = []
    if root is None:
        return result
    def postorder_helper(node):

        if node.left is not None:
            postorder_helper(node.left)
        if node.right is not None:
            postorder_helper(node.right)
        result.append(node.value)
    
    
    postorder_helper(root)
    return result


#-----------------------------Problem-11-------------------------------------
'''
108. Convert Sorted Array to Binary Search Tree
'''

def sorted_list_to_bst(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    
    if head is None:
        return None
    arr = head
    def sorted_list_to_bst_helper(arr,start,end):
        #base case
        if start > end: #no node left
            return None
        
        #recursive case
        mid = start + (end-start)//2
        newnode = BinaryTreeNode(arr[mid])
        newnode.left = sorted_list_to_bst_helper(arr,start,mid-1)
        newnode.right = sorted_list_to_bst_helper(arr,mid+1,end)
        
        return newnode
    
    res = sorted_list_to_bst_helper(arr,0,len(arr)-1)
    
    return res

sorted_list = {
"head": [-1, 2, 3, 5, 6, 7, 10]
}
#print(sorted_list_to_bst(sorted_list["head"]))


#------------------------------------Problem-12------------------------------
'''
Construct A Binary Search Tree From Its Preorder Traversal
'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def build_binary_search_tree(preorder):
    """
    Args:
     preorder(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    
    if not preorder:
        return None
    inorder = sorted(preorder)
    hashmap = {value:idx for idx,value in enumerate(inorder)}
    def build_binary_search_tree_helper(p,i,startp,endp,starti,endi):
        if starti>endi:
            return None
        
        #recursive case
        #find mid
        newnode = BinaryTreeNode(p[startp])
        midi = hashmap[p[startp]]
        num_left = midi -starti
        numright = endi - midi
        
        newnode.left = build_binary_search_tree_helper(p,i,startp+1,startp+num_left,starti,midi-1)
        newnode.right = build_binary_search_tree_helper(p,i,startp+1+num_left,endp,midi+1,endi)
        
        return newnode
    
    
    res = build_binary_search_tree_helper(preorder,inorder,0,len(preorder)-1,0,len(inorder)-1)
    return res
    
'''
Time Complexity - Leaf + intermediate 
                  Constnt +  O(n)
Space Complexity - Input + Aux + Output
                    O(n) + O(n) or O(logn) + O(n)
'''


#-------------------------------Problem-13------------------------------------  Not resolved
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def check_if_symmetric(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    # Write your code here.
    
    #Approch -1 Using Level Order Traversal
    
    if root is None:
        return True
    result = True
    q = [root]
    while q:
        len_q = len(q)
        slate = []
        for i in range(0,len_q):
            newnode = q.pop(0)
            slate.append(newnode.value)
            if newnode.left is not None:
                q.append(newnode.left)
            else:
                slate.append(-1)
            if newnode.right is not None:
                q.append(newnode.right)
            else:
                slate.append(-1)
        
        #check pallindrome
        if slate != slate[::-1]:
            result = False
            break
    return result


#------------------------Problem-14----------------------------------------
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    globalfound = []
    def dfs(node):
        afound , bfound = False,False
        #base case
        if node.left is None and node.right is None:
            if node.value == a:
                afound = True
            if node.value == b:
                bfound = True
            if afound and bfound and not globalfound:
                globalfound.append(node.value)
            return (afound,bfound)
        
        #recursive case

        if node.value == a:
            afound = True
        if node.value == b:
            bfound = True
        
        if node.left:
            p,q = dfs(node.left)
            afound = afound or p
            bfound = bfound or q
        if node.right:
            p,q = dfs(node.right)
            bfound = bfound or q
            afound = afound or p
            
        if afound and bfound and not globalfound:
            globalfound.append(node.value)
            
        return afound , bfound
            
    dfs(root)
    if globalfound:
        return globalfound[0]
    return 0

# data ={
# "root": [1, None,
# 3, 2, 5, None,
# None, None, 4]
# }
# run(data,lca,2,1)

#----------------------------Problem-15--------------------------------
'''
559. Maximum Depth of N-ary Tree
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(root) -> int:

        globalsol = []
        def dfs(node):
            if node is None :
                return 0
            
            #recursive case
            lr =rr = 0
            for child in node.children:
                lr = dfs(child)
                if lr  > rr:
                    rr = lr
            if globalsol:
                globalsol[0]= max(globalsol[0],rr+1) 
            else:
                globalsol.append(rr+1)
            return rr +1
        
        res = dfs(root)
    
        return res

#----------------------------Problem--------------------------------
'''
104. Maximum Depth of Binary Tree
'''

def maxDepth(root):
    
    if root is None:
        return 0
    
    def max_depth_helper(node):
        if node.left is None and node.right is None:
            return 1
        
        # recursive case
        lh = rh = 0
        if node.left:
            lh = max_depth_helper(node.left)
        
        if node.right:
            rh = max_depth_helper(node.right)
        
        #return solution
        return max(lh,rh)+1
    
    res = max_depth_helper(root)
    
    if not res:
        return 0
    return res
        

#----------------------------Problem-16--------------------------------
'''
230. Kth Smallest Element in a BST

'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def kth_smallest_element(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     int32
    """
    # Write your code here.
    
    if root is None:
        return 0
    globalk = [k]
    result = []
    def dfs(node):
        
        #base case 
        if node.left is None and node.right is None:
            pass

        #recursive case
        if node.left:
            dfs(node.left)
        
        globalk[0] = globalk[0] -1
        if globalk[0]==0:
            result.append(node.value)
        if node.right:
            dfs(node.right)
    
    dfs(root)
    if result:
        return result[0]
    return 0


data ={
"root": [5,3,6,2,4,None,None,1]
}
run(data,kth_smallest_element,k=3)