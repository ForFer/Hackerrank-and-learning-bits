"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/countingsort3
"""

n = int(input())
ar = []
cumFreq = [0]*100
for i in range(n):
    n = int(input().split()[0])
    ar.append(n)

for i in range(100):
    if i != 0:
        cumFreq[i] = cumFreq[i-1]+ar.count(i)
    else:
        cumFreq[i] = ar.count(i)
  
    
print(*cumFreq)
