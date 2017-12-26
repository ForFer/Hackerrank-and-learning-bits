"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
Unordered binary Tree implementation to be used by other python instances on this folder
"""

class Tree:
    def __init__(self, data=None):
        self.root = None
        self._length = 0


    def insert(self, data):
        if not self.root:
            self.root = data
            self._increment_length(1)


    @staticmethod
    def _increment_length(self, length):
        self._length += 1


    def get_length(self):
        return self._length

    
    def get_root(self):
        return self.root


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    

    def set_left(self, data):
        """
            Allow only left-right assignment of nodes
        """
        if isinstance(data, Node):
            self.left = data
            return 0
        else:
            return -1

    def set_right(self, data):
        """
            Allow only left-right assignment of nodes
        """
        if isinstance(data, Node):
            self.right= data
            return 0
        else:
            return -1
