"""
Author: Fernando Collado
Github: ForFer
"""


"""
There are N strings. Each string's length is no more than 20 characters.
There are Q also queries. For each query, you are given a string, and you need to find out
how many times this string occurred previously.

Input Format

The first line contains N, the number of strings.
The next lines N each contain a string.
The N+2nd line contains Q, the number of queries.
The following Q lines each contain a query string.

Sample Input

4
aba
baba
aba
xzxb
3
aba
xzxb
ab

Sample Output

2
1
0

"""

s=input()
i = int(s)
s = []
while(i>0):
    s.append(input())
    i=i-1

s1=input()
i = int(s1)
j = i
s1 = []
while(int(i)>0):
    s1.append(input())
    i=i-1
res = [0 for n in range(len(s1))]
for i in range(len(s1)):
    for j in range(len(s)):
        if(s1[i]==s[j]):
            res[i]+=1
    print(res[i])

"""
Better solution, by user georgeluisrocha

n = int(input())
strs = [input() for x in range(n)]
q = int(input())
for _ in range(q):
    print(strs.count(input()))

"""
