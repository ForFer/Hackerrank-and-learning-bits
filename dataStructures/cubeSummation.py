"""
Author: Fernando Collado
Github: ForFer
"""

"""

"""
# Working solution, but slow

# Proposed improvement: use dicts instead of nested list

reps = int(input())

sums = []
for _ in range(reps):
    n,ops = map(int, input().split())

    a = [ [[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for op in range(ops):
        s = input()
        if s[0] == 'U':
            pos= list(map(int,s[6:].split()))
            a[pos[0]-1][pos[1]-1][pos[2]-1] = pos[3]
        else:
            suma = 0
            p = list(map(int,s[5:].split()))
            for i in range(len(p)):
                p[i] = p[i] -1
            for i in range(p[0],p[3]+1):
                for j in range(p[1],p[4]+1):
                    for k in range(p[2],p[5]+1):
                        suma+= a[i][j][k]
            sums.append(suma)
    
for i in sums:
    print(i)
 
     
    
