"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
"""

m,n = list(map(int, input().split()))
string = input().split()
note = input().split()

d = dict()
for word in string:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
for word in note:
    if word in d:
        d[word] -= 1
        if d[word] >= 0:
            n -= 1

if n <= 0:
    print("Yes")
else:
    print("No")
    
