"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
Problem: https://www.hackerrank.com/challenges/qheap1
"""

from heapq import heappush, heappop, heapify

q = int(input())
h = []
res = []
for _ in range(q):
    #Posibility of getting one item, or two, if two, unpack them
    to_unpack = list(map(int,input().split()))

    if len(to_unpack) == 2:
        option, element = to_unpack
    else:
        option = to_unpack

    if option == 1:
        heappush(h,element)
    elif option == 2:
        h.pop(h.index(element))
        heapify(h)
    else:
        res.append(h[0])
    
for r in res:
    print(r)
