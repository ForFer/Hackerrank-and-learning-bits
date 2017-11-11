"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
"""

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    
    left_child = root.left
    right_child = root.right

    if left_child is None and right_child is None:
        return True
    elif left_child is None and right_child is not None:
        if right_child > root.data:
            return checkBST(root.right)
        else:
            return False
    elif left_child is not None and right_child is None:
        if left_child < root.data:
            return checkBST(root.left)
        else:
            return False
    else:
        if left_child < root.data and right_child > root.data:
            return checkBST(root.left) and checkBST(root.right)
        else:
            return False
            
            
