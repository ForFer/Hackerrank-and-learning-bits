"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def preOrder(root):
    data = preOrderTraverse(root)
    #print(data)
    return(data)


def preOrderTraverse(root):
    if root:
        node = str(root.data)
        if root.left:
            node = node + ' ' + preOrderTraverse(root.left)
        if root.right:
            node = node + ' ' + preOrderTraverse(root.right)
        return node
    else:
        return ''
