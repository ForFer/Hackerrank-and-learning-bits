"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/icecream-parlor
"""

t = int(input())

choosen = []
for _ in range(t):
    m = int(input())
    n = int(input())

    ice_creams = {i:int(x) for i,x in enumerate(input().split()) }

    found = False
    i = 0
    while not found:    
        current = ice_creams[i]
        if current > m:
            i+=1
            continue

        else:
            for j in range(i+1, n):
                ice_j = ice_creams[j]
                if current  + ice_j == m:
                    choosen.append([i+1,j+1])
                    found = True
            i+=1

for c in choosen:
    print(*c)

