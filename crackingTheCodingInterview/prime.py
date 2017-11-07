"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-big-o/problem
"""

import math

def is_prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False

    prime = True
    for j in range(3, int(math.sqrt(n))+1,2): 
        if n%j == 0:
            prime = False
            break
    return prime
 

t = int(input())

res = []
for _ in range(t):
    n = int(input())
    is_p = is_prime(n)  
    if is_p:
        res.append("Prime")
    else:
        res.append("Not prime")
   
for r in res:
    print(r)

