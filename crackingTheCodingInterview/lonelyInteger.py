"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-lonely-integer/problem
"""

n = int(input())

l = list(map(int, input().split()))

value = 0

for i in l:
    value ^= i

print(value)


"""
dict solution

d = dict()

for i in l:
    if i not in d:
        d[i] = 1
    else:
        del d[i]

print(*[k for k,x in d.items()])
"""
