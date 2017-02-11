"""
Author: Fernando Collado
Github: ForFer
"""

"""
We say that a string, s, contains the word hackerrank if a subsequence of the
characters in s spell the word hackerrank. For example, haacckkerrannkk does
contain hackerrank, but haacckkerannk does not (the characters all appear in the
same order, but it's missing a second r).

More formally, let p0,p1...,p9 be the respective indices of h, a, c, k, e, r, r, a, n, k in
string s. If p0<p1<...<p9 is true, then s contains hackerrank.

You must answer q queries, where each query i consists of a string, si. For each
query, print YES on a new line if contains hackerrank; otherwise, print NO
instead.

Input Format

The first line contains an integer denoting (the number of queries).
Each line of the subsequent lines contains a single string denoting .

Output Format

For each query, print YES on a new line if contains hackerrank; otherwise, print
NO instead.

Sample Input 0

2
hereiamstackerrank
hackerworld

Sample Output 0

YES
NO


"""

q = int(input())
hacker = "hackerrank"
res = []
for _ in range(q):
    s = input()
    index = -1
    found = 0
    for h in hacker:
        if h in s:
            found += 1
            index = s.index(h)
        else:
            break

    if len(hacker) == found:
        res.append("YES")
    else:
        res.append("NO")
for r in res:
    print(r)
