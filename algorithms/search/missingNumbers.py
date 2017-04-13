"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/missing-numbers
"""

n = int(input())
a = {}
for i in input().split():
    if i in a:
        a[i] += 1
    else:
        a[i] = 1

m = int(input())
missing = {}

for i in input().split():
    if i in a:
        a[i] -= 1
    else:
        missing[i] = 0

for i in a:
    if a[i] != 0:   
        missing[i] = 0

# In python3.6 sorted is unnecessary, as dict are ordered by default by key
#print(*[element for element in missing])
print(*[element for element in sorted(missing)])
