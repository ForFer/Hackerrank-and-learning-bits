"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-merge-sort/problem
"""

import math
from collections import deque


# Followed Skienna's book "The Algorithm Design Manual"
def mergesort(A, low, high):

    if low < high :
        midIndex = math.floor((low+high)/2)
        mergesort(A, low, midIndex)
        mergesort(A, midIndex+1, high)
        merge(A, low, midIndex, high)

def merge(A, low, middle, high):
    global swaps

    i = low

    d1 = deque(A[low:middle+1])
    d2 = deque(A[middle+1:high+1])
     
    while( d1 and d2 ):
        if d1[0] <= d2[0]:
            A[i] = d1.popleft()
            i += 1
        else:
            swaps += len(d2)
            A[i] = d2.popleft()
            i += 1
    while d1:
        A[i] = d1.popleft()
        i += 1
    while d2:
        A[i] = d2.popleft()
        i += 1

n = int(input()) # Number of arrays to sort
all_swaps = []
for _ in range(n):
    swaps = 0
    m = int(input())
    dataset = list(map(int, input().split()))
    
    mergesort(dataset, 0, m-1, )
    all_swaps.append(swaps)
print(*all_swaps)
