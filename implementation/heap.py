"""
Author: Fernando Collado
Github: ForFer
"""

#Heap implementation

import math

class Heap:

    def __init__(data = [], min_heap = True):
        self.data = data
        self.min_heap = min_heap

    def insert(data, heap):
        pass

    def get_child(parent, child=0):
        #child = 0 means left child, =1 right child
        index = 0
        if child == 0:
            index = parent*2+1
        else:   
            index = parent*2+2
            try:
                return self.data[index]
            else:
                return None

    def get_parent(child):
        try:
            return self.data[math.floor(child/2)-1]
        pass

    def get_min(heap):
        pass
    def get_max(heap):
        pass
