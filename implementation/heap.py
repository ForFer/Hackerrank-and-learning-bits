"""
Author: Fernando Collado
Github: ForFer
"""

#min Heap implementation

import math

class Heap:

    def __init__(self, data = [], min_heap = True):
        self.data = data
        self.min_heap = min_heap

    #Min heap, hence 
    def insert(self, data):
        self.data.insert(0,data)
        self.reorganize(0)

    #Get left child (= 0), or right child (= 1)
    def get_child(self, parent, child=0):
        index = 0
        if child == 0:
            index = parent*2+1
        else:   
            index = parent*2+2
        try:
            return self.data[index]
        except:
            return None

    def get_parent(self, child):
        try:
            return self.data[math.floor(child/2)-1]
        except:
            print("could not get parent of child %" % child)
        pass

    def get_min(self):
        return self.data[0]

    def get_max(self):
        
        pass

    
    def delete_root(self):
        #Swap root with last element, and delete it
        root = self.data[0]
        self.data[0] = self.data[len(self.data)]
        self.data.pop()

        #Start reorganizing tree from the root
        self.reorganize(0)

        return root

    def reorganize(self, level):

        #Equivalent to "if left child is none"
        if 2*level+1 >= len(self.data):
            return

        left_child = 2*level+1
        right_child = 2*level+2

        if right_child < len(self.data):

            successor = min(self.data[left_child], self.data[right_child])
        else:
            successor = self.data[left_child]

        #If the data of the next level is smaller than the current level
        # keep reorganizing recursively
        if self.data[level] > successor:        

            newLevel = self.data.index(successor)
            self.swap(level, newLevel)

            #Recursive call to organize successive levels
            self.reorganize(newLevel)
        

    #Ol'switcheroo
    def swap(self, new, old):
        temp = self.data[old]
        self.data[old] = self.data[new]
        self.data[new] = temp

    def __string__():
        print(*self.data)

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


 
