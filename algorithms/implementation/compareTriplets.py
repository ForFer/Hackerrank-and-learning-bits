"""
Author: Fernando Collado
Github: ForFer
"""

"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two
challenges, awarding points on a scale from to for three categories:
problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet A=(a0,a1,a2), and the
rating for Bob's challenge to be the triplet B=(b0,b1,b2).

Your task is to find their comparison scores by comparing a0 with b0, a1 with
b1, a2 and with b2.

    If ai>bi , then Alice is awarded 1 point.
    If ai<bi , then Bob is awarded 1 point.
    If ai=bi , then neither person receives a point.

Given A and B, can you compare the two challenges and print their respective
comparison points?

Input Format

The first line contains space-separated integers, a0, a1, and a2, describing the
respective values in triplet A.
The second line contains space-separated integers, b0, b1, and b2, describing the
respective values in triplet B.

Output Format

Print two space-separated integers denoting the respective comparison
scores earned by Alice and Bob.

Sample Input

5 6 7
3 6 10

Sample Output

1 1 

"""

A = list(map(int,input().split()))
B = list(map(int,input().split()))

points = [0 for _ in range(2)]

for i in range(len(A)):
    if A[i] < B [i]:
        points[1]+=1
    elif A[i] > B[i]:
        points[0]+=1
print(points[0], points[1])
