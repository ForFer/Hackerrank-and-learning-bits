"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation
"""
import collections

size, rotations = map(int, input().split())

array = list(map(int, input().split()))
d = collections.deque(array)
d.rotate(rotations*-1)

print(*list(d))

