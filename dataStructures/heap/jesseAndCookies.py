"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/jesse-and-cookies
"""

from heapq import heappush, heappop, heapify

n,k = list(map(int,input().split()))
h = []
cookies = list(map(int,input().split()))

for cookie in cookies:
    heappush(h, cookie)

sum_k = 0
steps = 0
finished = False
while h:
    steps += 1
    sum_k = h[0]

    if len(h) > 1:
        if len(h) > 2:
            sum_k += 2*min(h[1],h[2])
            if h[1] < h[2]:
                h = h[2:]
            else:
                h = h[1:1] + h[3:]
        else:
            sum_k += h[1]
            h.pop()
            h.pop()
    heapify(h)
    if sum_k >= k:
        print(steps)
        finished = True
        break
        
if not finished:
    print(-1)


