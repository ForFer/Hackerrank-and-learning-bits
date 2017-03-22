"""
Author: Fernando Collado
Github: ForFer
"""

#min Heap implementation adapted to prim's algorithm

from math import floor

class Node:
        
    def __init__(self, label, data):
        self.data = data
        self.label = label

class Heap:

    def __init__(self, data = None):
        if data is None:
            data = []
        self.data = data
        self.from_to = {}
        self.visited = []

    #Min heap, hence 
    def insert(self, data):
        self.data.append(data)
        self.reheapify( index=int(floor(len(self.data)/2)), option=1 )

    def get_min(self):
        return self.data[0]

    def get_max(self):
        return max(self.data[int(len(self.data)/2):]) 

    def extract_min(self):
        #Swap root with last element, and delete it
        root = self.data[0]
        self.data[0] = self.data[len(self.data)-1]
        self.data.pop()

        #Start reorganizing tree from the root
        self.reheapify( index=int(floor(len(self.data)/2)), option=0 )

        return root

    def reheapify(self, index, option):
        """
        reheapify down (option=0), or up(option=1) 
        """
        stop = False

        if option==0:
            n = 0
            stop_n = index
        else:
            n = index
            stop_n = 0
        while not stop: 
            parent = self.data[n].data
            left_child = self.data[2*n+1].data if len(self.data)-1>=2*n+1 else None
            right_child = self.data[2*n+2].data if len(self.data)-1>=2*n+2 else None

            toSwap = None            

            if left_child is not None and right_child is not None:
                if parent > min(left_child, right_child):
                    if left_child < right_child:
                        toSwap = 2*n+1 #left child
                    else:
                        toSwap = 2*n+2 #right child
            else:
                if left_child is not None and right_child is None:
                    if parent > left_child:
                        toSwap = 2*n+1 #left child
                elif right_child is None and left_child is not None:
                    if parent > right_child:
                        toSwap = 2*n+2 #right_child

            if toSwap:
                self.swap(n, toSwap)

            if option==0:
                n += 1
                if n > stop_n:
                    stop = True
            else:
                n -= 1
                if n < stop_n:
                    stop = True
    
    #Ol'switcheroo, pythonic style
    def swap(self, new, old):
        self.data[old], self.data[new] = self.data[new], self.data[old]

    def __str__(self):
        s = ''
        for i in self.data:
            temp = "Label: " + str(i.label) + " data: " + str(i.data) +"\n"
            s += temp
        return s

def prim(start, graph):
    #h = Heap()
    print(graph)

    distances = Heap()
    for label in graph:
        if label is not start:
            node = Node(label, float('Inf'))
        else:
            node = Node(label, 0)
        distances.insert(node)

    from_to = {}

    vertix = h.extract_min()
    
    #min 7:32  

    return None


def test():
    graph = {
        'A' : {'B':3, 'D':1},
        'B' : {'A':3, 'C':1, 'D':3},
        'C' : {'B':1, 'D':1, 'F':4},
        'D' : {'A':1, 'C':1, 'E':6},
        'E' : {'C':5, 'D':6, 'F':2},
        'F' : {'C':4, 'E':2}
        }

    mst = prim('A', graph)

    #assert
        
if __name__=="__main__":
    test()


 
