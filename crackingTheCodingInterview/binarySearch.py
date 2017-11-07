"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
"""


t = int(input())

for _ in range(t):
    money = int(input())
    flavours = int(input())
    costs = list(map(int, input().split()))
    d = dict()
    for i, cost in enumerate(costs):
        money_left = money - cost
        if money_left in d.keys():
            print(d[money_left]+1, i+1)
        else:
            d[cost] = i
    
    
