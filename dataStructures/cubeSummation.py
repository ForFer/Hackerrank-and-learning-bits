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
    updated = set()
    for op in range(ops):
        s = input()
        if s[0] == 'U':
            x,y,z, value= list(map(int,s[6:].split()))
            a[x-1][y-1][z-1] = value
            updated.add((x-1, y-1, z-1))
        else:
            suma = 0
            p = list(map(int,s[5:].split()))
            x1,y1,z1,x2,y2,z2 = p
            cells = []
            for (x,y,z) in updated:
                if x1-1 <= x and x2 > x and y1-1 <= y and y2 > y and z >= z1-1 and z < z2:
                    cells.append((x,y,z))
            for (x,y,z) in cells:
                suma += a[x][y][z]
                
            sums.append(suma)
    
for i in sums:
    print(i)
 
     
    
