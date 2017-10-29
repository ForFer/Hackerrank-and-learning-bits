"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-making-anagrams
"""

def number_needed(a, b):
    d = dict()
    for letter in a:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    for letter in b:
        if letter in d:
            d[letter] -= 1
        else:
            d[letter] = -1

    total_changes = 0
    for k in d:
        total_changes += abs(d[k])

    return total_changes


a = input()
b = input()
print(number_needed(a,b))

