"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/merging-communities
"""

#TODO: make faster

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

def size_dset(data, element):
    # This method returns the size of the set to which element belongs
    if element.parent == element:
        return 1
    else:
        siz = 0
        for d in data:
            if data[d].parent == element.parent:
                siz+=1
        return siz

n, q = list(map(int, input().split()))

data = {}
for i in range(n):
    node = Node(i)
    data[i] = node
    makeSet(node)    

res = []
for _ in range(q):
    query = input().split()
    if query[0] == 'Q':
        res.append( size_dset(data, data[int(query[1])-1]) )
    elif query[0] == 'M':
        el1 = data[int(query[1])-1]
        el2 = data[int(query[2])-1]
        union(el1, el2)

for r in res:
    print(r)
