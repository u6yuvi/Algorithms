
from collections import deque

def input_int32(data):
    argument = int(data)
    return argument


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def input_BinaryTreeNode_int32(data):
    argument = None # Root of the tree that we return.
    nodes_with_uninitialized_children = deque()
    next_child_is_left = True
    for json_array_item in data:
        if json_array_item is None:
            new_node = None
        else:
            new_node = BinaryTreeNode(input_int32(json_array_item))
            if argument is None:
                argument = new_node
        if nodes_with_uninitialized_children:
            parent_node = nodes_with_uninitialized_children.popleft()
            if next_child_is_left:
                parent_node.left = new_node
            else:
                parent_node.right = new_node
            next_child_is_left = not next_child_is_left
        if new_node is not None:
            nodes_with_uninitialized_children.extend([new_node, new_node])
    return argument

