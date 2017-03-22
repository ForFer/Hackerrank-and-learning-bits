"""
Author: Fernando Collado
Github: ForFer
"""

#min Heap implementation

from math import floor

class Heap:

    def __init__(self, data = None):
        if data is None:
            data = []
        self.data = data

    #Min heap, hence 
    def insert(self, data):
        self.data.append(data)
        self.reheapify( index=int(floor(len(self.data)/2)), option=1 )

    def get_min(self):
        return self.data[0]

    def get_max(self):
        return max(self.data[int(len(self.data)/2):]) 

    def delete_root(self):
        #Swap root with last element, and delete it
        root = self.data[0]
        self.data[0] = self.data[len(self.data)-1]
        self.data.pop()

        #Start reorganizing tree from the root
        self.reheapify( index=int(floor(len(self.data)/2)), option=0 )

        return root

#    def delete_item(self, element):
#        for i,d in enumerate(self.data):
#            if d == element:
#                self.data = self.data[:i] + self.data[i+1:]
#        self.reheapify(index=int(floor(len(self.data)/2)), option=1)


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
            parent = self.data[n]
            left_child = self.data[2*n+1] if len(self.data)-1>=2*n+1 else None
            right_child = self.data[2*n+2] if len(self.data)-1>=2*n+2 else None

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
    print(h.data)
    print("getting root ", h.delete_root())
    print("heap after deletion ", h.data)
    h.delete_item(50)
    print("Removing element 50")
    print("Heap after deletion", h.data)
        
if __name__=="__main__":
    test()


 
