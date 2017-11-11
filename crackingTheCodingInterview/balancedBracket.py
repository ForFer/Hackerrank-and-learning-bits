"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
"""

def is_matched(expression):
    
    if len(string)%2 == 0:
        d = {'{':'}', '[':']', '(':')' }
        stack = []
        for c in string:
            if c in d:
                stack.append(d[c])
            elif not stack or c != stack.pop():
                return False
        return not stack

    else:
        return False


q = int(input())

results = []
for _ in range(q):
    string = input()
    results.append("YES" if is_matched(string) else "NO")
    
for r in results:
    print(r)
