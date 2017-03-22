"""
Author: Fernando Collado Egea
Github: ForFer

Note: This algorithm is correct, and it yields the proper result, but it
happens to have timeouts (python is not as fast as other language :C )

"""

"""
You are given a list of size N, initialized with zeroes. You have to perform M 
operations on the list and output the maximum of final values of all the N
elements in the list. For every operation, you are given three integers a,b and
k and you have to add value k to all the elements ranging from index a to b (both
inclusive).

Input Format

First line will contain two integers and separated by a single space.
Next lines will contain three integers , and separated by a single space.
Numbers in list are numbered from to .

Output Format

A single line containing maximum value in the updated list.

Sample Input

5 3
1 2 100
2 5 100
3 4 100

Sample Output

200

"""

N,M = map(int,input().split())
out = [0 for x in range(int(N))]

for _ in range(M):
    a,b,k = map(int,input().split())
    if(a==b):
        out[a-1]+=k
    else:
        for i in range(a-1,b):
            out[i]+=k

print(max(out))
