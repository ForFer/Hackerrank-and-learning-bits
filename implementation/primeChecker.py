"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
Objective
Today we're learning about running time! Check out the Tutorial tab for learning
materials and an instructional video!

Task
A prime is a natural number greater than 1 that has no positive divisors other
than 1 and itself. Given a number, n, determine and print whether it's
Prime or Not prime.

Note: If possible, try to come up with a O(sqrt(n)) primality algorithm, or see what sort
of optimizations you come up with for an O(n) algorithm. Be sure to check out the
Editorial after submitting your code!

Input Format

The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines contains an integer, n, to be tested for primality.

Output Format

For each test case, print whether n is Prime or Not prime on a new line.

Sample Input

3
12
5
7

Sample Output

Not prime
Prime
Prime

"""
import math

def is_prime(n):
    if n==1 or n%2==0:
        return False
    elif n==2:
        return True

    is_prime = True
    for j in range(3, int(math.sqrt(n))+1,2): 
        if n%j == 0:
            is_prime = False
            break
    return is_prime
 

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
