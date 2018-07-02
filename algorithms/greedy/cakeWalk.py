"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/marcs-cakewalk/problem
"""

n = int(input())
cupcakes = list(map(int, input().split()))

cupcakes.sort(reverse=True)
print(sum([c*2**j for j,c in enumerate(cupcakes)]))
