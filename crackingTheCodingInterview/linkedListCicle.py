"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
"""

# Working with some given code
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the
list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

# Basically, check with two pointers alternatively the next position, and 2
# ahead. If there is a cycle, they will meet
def has_cycle(head):
    pointer_0 = head
    pointer_1 = head.next
    
    while pointer_0 is not None and pointer_1 is not None:
        if pointer_0 == pointer_1:
            return 1
        else:
            pointer_0 = pointer_0.next
            pointer_1 = pointer_1.next.next
    return 0  
