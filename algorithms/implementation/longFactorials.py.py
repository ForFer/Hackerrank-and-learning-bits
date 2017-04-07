"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/extra-long-factorials
"""

# The result of this problem in python is trivial

n = int(input().strip())
res = 1
for i in range(n, 1, -1):
    res *= i
print(res)
