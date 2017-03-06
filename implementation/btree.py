class Node:
    """
    Class Node
    """
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """
    def __init__(self, node):
        self.root = node

    def createNode(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, node , data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """

        #if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side

        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node

    def search_node(self, root, data):
        q = []
        q.append(root)
        found = False
        while(q):
            node =  q.pop(0)
            if node.data == data :
                return node
            if node.left is not None:
                q.append(node.left)    
            if node.right is not None:
                q.append(node.right)

        return None

    def level_order_traversal(self, root):
        q = []
        order = []
        q.append(root)
        while q:
            node = q.pop(0)
            order.append(node.data)
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
                
        return order

    def getHeight(self,root):
        if not root:
            return -1
        else:
            return 1+max(self.getHeight(root.left), self.getHeight(root.right)
        

def Main():
    
    node = Node(v1)
    tree = Tree(node)
    root = tree.root
        
    tree.insert(root,v2)
        
    snode = tree.search_node(root,s)
          
   
    queue = []
    queue.append(snode)
    while(queue):
        print(node.data)
        node = queue.pop(0)
        if node.data == i+1 : 
            found=node.data
            break
        if node.left != None :
            queue.append(node.left)    
        if node.right != None :
            queue.append(node.right)
        
    
if __name__=="__main__":
    Main()
