"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/countingsort4
"""

n = int(input())
ar = {}

for i in range(n):
    line = input().split()
    if n/2 > i:
        line[1] = '-'
    if int(line[0]) in ar:
        ar[int(line[0])] += line[1] + ' '
    else:
        ar[int(line[0])] = line[1] + ' '
        
s = ''
for k in ar:
    s += ar[k]
print(s)
