"""
Author: Fernando Collado
Github: ForFer
"""

"""
Heapsort implementation, source: https://en.wikipedia.org/wiki/Heapsort
"""

import math

def heapsort(l):
    count = len(l)
    heapify(l,count)

    end = count-1

    i = 1

    while end>0:    
        Swap(0, end, l)
        end-=1
        shiftDown(l, 0, end)

        print("Iteration", i, ": ", l)
        i+=1


def heapify(l, count):
    start = parent(count)

    while start >= 0:
        shiftDown(l, start, count-1)
        start-=1
        
def shiftDown(l, start, end):
    root = start

    while leftChild(root) <= end:
        child = leftChild(root)
        swap = root

        if l[swap] < l[child]:
            swap = child
        if child+1<=end and l[swap] < l[child+1]:
            swap = child+1
        if swap == root:
            return
        else:
            Swap(root, swap, l)
            root = swap

def leftChild(element):
    return element*2+1

def parent(element):
    return math.floor((element-1)/2) 

def Swap(i,j,l):
    temp = l[j]
    l[j] = l[i]
    l[i] = temp


a = [12,-8,68,0, 11, 3, 35, 1]  
print(a)
heapsort(a)
print(a)
