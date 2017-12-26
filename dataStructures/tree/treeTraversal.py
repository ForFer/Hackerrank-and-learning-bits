"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4

Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def postOrder(root):
    data = postOrderTraverse(root)
    #print(' '.join(str(n) for n in data))
    return data


def postOrderTraverse(root):
    if root:
        node = []
        if root.left:
            node += postOrderTraverse(root.left)
        if root.right:
            node +=  postOrderTraverse(root.right)
        node.append(root.data)
        return node
    else:
        return []


def preOrder(root):
    data = preOrderTraverse(root)
    #print(' '.join(str(n) for n in data))
    return data


def preOrderTraverse(root):
    if root:
        node = []
        node.append(root.data)
        if root.left:
            node += preOrderTraverse(root.left)
        if root.right:
            node +=  preOrderTraverse(root.right)
        return node
    else:
        return [] 


def inOrder(root):
    data = inOrderTraverse(root)
    #print(' '.join(str(n) for n in data))
    return data


def inOrderTraverse(root):
    if root:
        node = []
        if root.left:
            node += inOrderTraverse(root.left)
            
        node.append(root.data)
        
        if root.right:
            node +=  inOrderTraverse(root.right)
        return node
    else:
        return []  
