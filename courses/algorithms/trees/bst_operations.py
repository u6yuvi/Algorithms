from utils import input_BinaryTreeNode_int32
from utils import BinaryTreeNode
from typing import List


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def run(data,func,**args):
    root = input_BinaryTreeNode_int32(data["root"])
    print(func(root,**args))

#-------------------------Problem-1---------------------------------------
'''
Search A Node In Binary Search Tree
'''

def search_node_in_bst(root, value):
    """
    Args:
     root(BinaryTreeNode_int32)
     value(int32)
    Returns:
     bool
    """
    '''
    T(n) = For balanced Binary Search Tree - O(log(n)) 
    T(n) = O(n) - worst case when it is not balanced
    '''
    
    if root is None:
        return False
    
    curr = root
    while curr is not None:
        if curr.value == value:
            return True
        elif curr.value > value:
            curr = curr.left
        elif curr.value < value:
            curr = curr.right
    
    return False

#-------------------------Problem-2---------------------------------------
'''
Build a Tree [ Insert n elemetns in a tree]
'''
def build_a_bst(values):
    """
    Args:
     values(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    
    val = values[0]
    root = BinaryTreeNode(val)
    
    
    for k in values[1:]:
        prev = None
        curr = root
        while curr is not None:
            #all values are distinct
            #if k == curr.value
            
            #check left node and incrememnt the pointer
            if k < curr.value:
                prev = curr
                curr = curr.left
                
            #check right node and increment the pointer
            elif k> curr.value:
                prev = curr
                curr = curr.right
            
        #link previous node with the new node
        if k< prev.value:
            prev.left = BinaryTreeNode(k)
        elif k > prev.value:
            prev.right = BinaryTreeNode(k)
            
        
        
    return root

#-------------------------Problem-3---------------------------------------
'''
BST - Max value

'''
def get_maximum_value(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    #1st method
    
    # if root is None:
    #     return 0
    # curr = root
    # prev= None
    # while curr is not None:
    #     prev = curr
    #     curr = curr.right
    
    
    # return prev.value

    # 2nd method  - slightly optimised
    if root is None:
        return 0
    curr = root
    while curr.right is not None:
        curr = curr.right
        
    return curr.value


data = {
"root": [2,
1, 5,
None, None, 4, 6]
} # Breadth First Approach representation of Tree
root = input_BinaryTreeNode_int32(data["root"])
print("Max Value",get_maximum_value(root=root))


#-------------------------Problem-3---------------------------------------
'''
BST - Successor

'''