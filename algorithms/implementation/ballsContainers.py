"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
"""

q = int(input())
for _ in range(q):
    n = int(input())
    hsum = [0 for _ in range(n)]
    vsum = [0 for _ in range(n)]
    for i in range(n):
        line = list(map(int, input().split()))
        vsum[i] += sum(line)
        for j in range(n):
            hsum[j] += line[j]
    if sorted(hsum) == sorted(vsum):
        print("Possible")
    else:
        print("Impossible")
