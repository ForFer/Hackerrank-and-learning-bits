"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem
"""

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:    
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fibo_memo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_memo(n-1) + fibo_memo(n-2)

n = int(input())

print(fibo_memo(n))
