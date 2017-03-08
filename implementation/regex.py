"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
Day 28 of 30-day challenge
"""

import re

N = int(input())
names = []
for _ in range(N):
    firstName,emailID = input().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]

    match = re.match(".+@gmail.com", emailID)
    if match:
        names.append(firstName)

names.sort()
for name in names:
    print(name)
