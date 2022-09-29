# Linked List
'''
Made up of independent nodes that may contain any type of data 
and each node has a reference to the next node in the link.

Not stored in contiguous block
Node consists of data and reference
Head node which has reference to the starting node.
Tail - node with reference to the last element in the linked list.
Last node - Node with null reference 
'''

#Linked List vs Arrays
'''
Linked List
1. Each node is independent and can be deleted.
2. Donot have to define the size of the linked_list
3. Insertion and deletion of an element is not O(n)
4. Accessing the element is not that efficient.
Array
1. Element can be deleted but the empty cell in contiguous block will 
still exists.
2. The size of the array is predefined.
3. Insertion and deletion of an element is very efficient.
4. Accessing the element is very efficient 

'''

# create a Lineked List with two nodes

from platform import node


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class SlinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self) -> None:
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self,value,location):
        # create new node
        newnode = Node(value)
        if self.head is None: # if no node in the SLL
            self.head = newnode
            self.tail = newnode

        if location==0: # insert in the beginnning
            # old head->new node
            #newnode_next = self.head
            newnode.next = self.head
            self.head = newnode
            
        elif location ==-1: #insertion in the end
            newnode.next = None
            self.tail.next = newnode
            self.tail = newnode   
        else:
            tempnode = self.head
            i = 0
            while i< location-1: # iterate to the last element
                tempnode = tempnode.next
                i+= 1
            nextnode = tempnode.next
            newnode.next = nextnode
            tempnode.next = newnode
            if tempnode == self.tail:
                self.tail = newnode






n1 = Node(2)
n2 = Node(3)
sll = SlinkedList()
sll.head = n1
sll.head.next = n2
sll.tail = n2

print([node.value for node in sll])
