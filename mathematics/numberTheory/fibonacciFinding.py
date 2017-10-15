"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/fibonacci-finding-easy
"""


def fibo(a, b, n):
        temp = []
        temp.append(a)
        temp.append(b)
        if n<2:
            return temp[n]
        else:
            for i in range(2, n+1):
                temp.append(temp[i-1] + temp[i-2])
            return temp[n]


t = int(input())

res = []
for _ in range(t):
    a,b,n = list(map(int, input().split()))
    res.append(fibo(a, b, n))
    
for r in res:
    print(r)

