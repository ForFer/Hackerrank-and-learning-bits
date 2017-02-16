"""
Author: Fernando Collado
Github: ForFer
"""

"""
Same problem as before, but now the output is the actual numbers ordered, not
count
"""

n = int(input())

ar = list(map(int, input().split()))
count = []
s = ''
for i in range(100):
    for n in range(ar.count(i)):
        s += str(i) + ' '

print(s)
