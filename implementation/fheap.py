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
        self.child = None
        self.degree = 0

class Heap:

    def __init__(self):
        self.root_list = None
        self.n_elements = 0
        self.min_element = None



    #Min heap, hence 
    def insert(self, data):
        
        node = Node(data)

        if not self.min_element:
            self.root_list = node
            self.min_element = node
        else:
            #If new node is min, insert at pos 0, else, just append it
            if node.data < self.min_element.data:
                self.min_element = node
            #If there is more than 1 node in the root list
            if self.root.right:
                self.root.right.left = node
                node.right = self.root_list.right 

            self.root_list.right = node
            node.left = self.root_list

        self.n_elements += 1

    def merge(self, heap):
        root_right = self.root_list.right
        self.root_list.right = heap.root_list
        heap_right = heap.root_list.right
        heap_left = heap.root_list.left
        
        
        
        if not self.min_element or (
            heap.min_element!=None and heap.min_element.data<self.min_element.data):
            self.min_element = heap.min_element

        self.n_elements += heap.n_elements

    #Iterator through the circular doubly linked list
    def iterate(self, start):
        node = start
        stop = start
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right

    def extract_min(self):

        m = self.min_elements

        if not m:
            if not m.child
                children = [x for x in self.iterate(m.child)]
                for i in range(len(children)):
                    self.merge_root(children[i])
                    children[i].parent = None
            self.remove_from_root(m)

            if m = m.right:
                self.min_element = self.root_list = None
            else:
                self.min_element = m.right
                self.consolidate()
            self.n_elements-=1
        return m

    def insert(self, data):
        pass

    def decrease_key(self, x, k):
        pass

    def merge(self, heap):
        pass

    def merge_with_root(self, node):
        pass

    def remove_from_root(self, node):
        pass

    def consolidate(self):
        pass

    def get_min(self):
        return self.min_element

  

    #TODO: is this even correct??????????
    def swap_root_list(self, new, old):
        self.root_list[old], self.root_list[new] = self.root_list[new], \
            self.root_list[old]

#        temp = self.root_list[old]
#        self.root_list[old] = self.root_list[new]
#        self.root_list[new] = temp


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


 
