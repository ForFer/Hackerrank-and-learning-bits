"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
Implementation of a disjoint set from scratch, to be used in other hackerrank
problems involving disjoint sets

Source: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.rank = None
        self.parent = None

def makeSet(x):
    'Receives an isolated node, and makes a new set with it'
    x.parent = x
    x.rank = 0
    
def union(x, y):
    """
    Gets 2 nodes, checks if they belong to the same set, if they dont, merge

    Parameters
    ----------
    x, y are both nodes to make the union with

    Returns 
    ----------
    0 if they were already together
    -1 if there were some error
    1 if union was successful

    """
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return 0

    if x_root.rank < y_root.rank:
        x_root.parent = y_root
        return 1
    elif x_root.rank > y_root.rank:
        y_root.parent = x_root
        return 1
    else:
        y_root.parent = x_root
        x_root.rank = x_root.rank + 1
        return 1

    return -1 # If code gets to this point, there was some error


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def to_str(data):
    groups = {}

    # Find root elements, create one entry in dict for each
    for d in data:
        if d.parent == d:
            groups[d.data] = [d.data]
    # Associate elements with their parents
    for d in data:
        if d.parent != d:
            groups[d.parent.data].append(d.data)

    for i,g in enumerate(groups):
        print("Group ",i,": ", *groups[g])


def test():
    data = []
    for i in range(5):
        node = Node(i)
        data.append(node)
        makeSet(node)
   
    r1 = union(data[0], data[1])
    r2 = union(data[0], data[1])
    r3 = union(data[0], data[2])
    r4 = union(data[3], data[4])

    to_str(data)

    assert r1 # 1
    assert not r2 # 0
    assert r3 # 1
    assert r4 # 1
    

if __name__=="__main__":
    test()
