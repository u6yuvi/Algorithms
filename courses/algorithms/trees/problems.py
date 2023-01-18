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


data = {
"root": [0,
1, 2,
3, 4]
}

run(data,right_view)