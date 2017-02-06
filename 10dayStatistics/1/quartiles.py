
"""
Author: Fernando Collado
Github: ForFer
"""

"""
Task
Given an array, X, of n integers, calculate the respective first quartile (Q1),
second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2,
and Q3 are integers.

Input Format

The first line contains an integer, n, denoting the number of elements in the
array.
The second line contains n space-separated integers describing the array's
elements.

Output Format

Print lines of output in the following order:

    The first line should be the value of Q1.
    The second line should be the value of Q2.
    The third line should be the value of Q3.

Sample Input

9
3 7 8 5 12 14 21 13 18

Sample Output

6
12
16

"""
def calculateQuartile(array):
    q = -1
    if(len(array)%2!=0):
        q = array[len(array)//2]
    else:
        q = ( array[len(array)//2-1] + array[len(array)//2] ) / 2
    return q



n = int(input())
values = list(map(int,input().split()))
values = sorted(values)
#Naive implementation

Q = [0 for _ in range(3)]
lower = []
higher = []
if(n%2!=0):
    Q[1] = values[n//2]
    lower = values[0:n//2]
    higher = values[n//2+1:]
else:
    Q[1] = ( values[n//2-1] + values[n//2] ) / 2
    lower = values[0:n//2]
    higher = values[n//2:]


Q[0] = calculateQuartile(lower)
Q[2] = calculateQuartile(higher)

for q in Q:
    print(int(q))


