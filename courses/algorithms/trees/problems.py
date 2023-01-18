from utils import input_BinaryTreeNode_int32

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

def run(data,func):
    root = input_BinaryTreeNode_int32(data["root"])
    print(func(root))


#-------------------Problem-1--------------------------------------------------
'''
Level Order Traversal on Binary Tree

'''
def level_order_traversal(root):
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
Level Order Traversal for N-ary tree
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
Right side view of the binary tree
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
        result.append(temp)
    return result

#---------------------------------Problem-3-----------------------------------------------

'''
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
Zig-Zag Level Orer Traversal
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


#-------------------------Problem-5-----------------------------------------

'''
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
    # Write your code here.

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
    # Write your code here.
    result = False
    if root is None:
        return result
    def helper_path_sum(node,target):
        #base case
        if node.left is None and node.right is None:
            if target==node.value:
                result.append(True)
        
        #recursive case
        if node.left is not None:
            helper_path_sum(node.left,target-node.value)
        if node.right is not None:
            helper_path_sum(node.right,target-node.value)
        
            
    helper_path_sum(root,k)
    if result:
        return result[0]
        
'''
Worst Case Scenario is when it is a balanced binary tree as in that case there \
could be n/2[number of leaf nodes] such paths with each of size log(n)[height]

Time Complexity - Leaf Node + Intermediate node
                  O(nlog(n)) + Constant Work
Space Complexity - Input + Aux + Ouptut
                            O(log(n)) + O(nlog(n))
'''


data = {
"root": [0,
1, 2,
3, 4]
}

run(data,right_view)