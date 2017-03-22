"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
Problem: https://www.hackerrank.com/challenges/array-left-rotation
"""

from collections import deque

n,r = list(map(int, input().split()))

d = deque(list(map(int,input().split())))
d.rotate(-1*r)
print(*d)
