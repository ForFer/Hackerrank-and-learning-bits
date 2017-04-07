"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/closest-numbers
"""

n = int(input())
ar = list(map(int, input().split()))

ar.sort()

pairs = []
minDis = 9223372036854775807
for i in range(len(ar)-1):
    if ar[i+1]-ar[i] < minDis:
        minDis = ar[i+1] - ar[i]
for i in range(len(ar)-1):
    if ar[i+1]-ar[i] == minDis:
        pairs.append(ar[i])
        pairs.append(ar[i+1])
        
print(*pairs)
