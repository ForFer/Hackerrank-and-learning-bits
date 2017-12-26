"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
Test for the tree implementation
"""

from tree import Node, Tree
from treeTraversal import preOrder, postOrder, inOrder


def test(root):
    assert(root.set_left(1) == -1)


def print_test_tree(root):
    #TODO: finish print tree
    print(" "*2, root.data)
   

def test_preorder(root):
    preorder = preOrder(root)
    assert(preorder == [1, 2, 4, 5, 3, 6, 7])


def test_postorder(root):
    postorder = postOrder(root)
    assert(postorder == [4, 5, 2, 6, 7, 3, 1])

def test_inorder(root):
    inorder = inOrder(root)
    assert(inorder == [4, 2, 5, 1, 6, 3, 7])


if __name__ == "__main__":
    root = Node(1)
    t = Tree(root)
    left_child = Node(2)
    right_child = Node(3)
    root.set_left(left_child)
    root.set_right(right_child)
    left_child.set_left(Node(4))
    left_child.set_right(Node(5))
    right_child.set_left(Node(6))
    right_child.set_right(Node(7))
  
    test(root) 
    test_preorder(root)    
    test_postorder(root)    
    test_inorder(root)    
    
    #print_test_tree(root)
