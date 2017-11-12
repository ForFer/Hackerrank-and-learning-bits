"""
Author: Fernando Collado
Github: ForFer
"""

#min Heap implementation
#TODO
# - add delete_item
# - fix get_max

from math import floor

class Heap:

    def __init__(self, data = None):
        if data is None:
            data = []
        self.data = data

    #Min heap, hence 
    def insert(self, data):
        print("insert:",data)
        print("heap before", self.data)
        self.data.append(data)
        self.heapifyUp()
        print("Heap after", self.data)

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
        self.heapifyDown()

        return root

#    def delete_item(self, element):
#        for i,d in enumerate(self.data):
#            if d == element:
#                self.data = self.data[:i] + self.data[i+1:]
#        self.reheapify(index=int(floor(len(self.data)/2)), option=1)

    def heapifyUp(self):
        index = len(self.data)-1
        parent = floor((index-1)/2)
    
        while index > 0:
            if self.data[parent] > self.data[index]:
                self.swap(parent, index)
                index = parent
                parent = floor((index-1)/2)
            else:   
                index = -1

    def heapifyDown(self):
        index = 0
        stop = False
    
        while not stop:
            current = self.data[index]
            left = self.data[index*2+1] if len(self.data)-1 >= 2*index+1 else None
            right = self.data[index*2+2] if len(self.data)-1 >= 2*index+2 else None

            if left and right:
                if current > min(left, right):
                    if left < current:
                        self.swap(index*2+1, index)
                    elif right < current:
                        self.swap(index*2+2, index)
                else:
                    stop = True
            else:
                if left and not right:
                    if left < current:
                        self.swap(index*2+1, index)
                elif not left and right:
                    if right < current:
                        self.swap(index*2+2, index)
                else:
                    stop = True

            index = index*2+1
   
    #Ol'switcheroo, pythonic style
    def swap(self, new, old):
        self.data[old], self.data[new] = self.data[new], self.data[old]

    def __string__():
        print(*self.data)

def test():
    h = Heap()
    
    h.insert(-1)
    print(h.data)

    h.insert(1)
    print(h.data)

    for i in range(2,5):
        h.insert(i)
        print(h.data)


    h.insert(0)
    print(h.data)

    h.insert(-15)
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
#    h.delete_item(50)
#    print("Removing element 50")
#    print("Heap after deletion", h.data)
        
if __name__=="__main__":
    test()


 
