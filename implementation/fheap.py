"""
Author: Fernando Collado
Github: ForFer
"""

#min fibonacci heap implementation

import math

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.mark = False
        self.degree = 0

class Heap:

    def __init__(self):
        self.root_list = None
        self.root_values = []
        self.n_elements = 0
        self.min_element = None

    #Min heap, hence 
    def insert(self, data):
        
        node = Node(data)

        if not self.min_element:
            self.insert_at_root(node)
            self.min_element = data
        else:
            self.insert_at_root(node)
            if node.data < self.min_element:
                self.min_element = node.data
        self.n_elements += 1

    def insert_at_root(self, node):
        #If root list is empty, create it with the node
        if not self.root_list:
            self.root_list = node
            self.root_values.append(node.data)
        #If list is not empty, add new node to list of root nodes
        else:
            temp = self.root_list.right
            self.root_list.right = node
            node.left = self.root_list
            node.right = temp
            self.root_values.insert(1,data)


    #Get left child (= 0), or right child (= 1)
    def get_child(self, node):
        return None

    def get_parent(self, child):
        return self.data[math.floor(child/2)-1]

    def get_min(self):
        return self.data[0]

    def get_max(self):
        return max(self.data[int(len(self.data)/2):]) 
       

    #Ol'switcheroo
    def swap(self, new, old):
        temp = self.data[old]
        self.data[old] = self.data[new]
        self.data[new] = temp



def test():
    h = Heap()
    
    h.insert(1)
    print(h.data)

    for i in range(2,5):
        h.insert(i)
        print(h.data)


    h.insert(0)
    print(h.data)

    h.insert(50)
    print(h.data)

    h.insert(-1)
    print(h.data)

    print(h.get_min())
    print(h.get_max())


        
if __name__=="__main__":
    test()


 
