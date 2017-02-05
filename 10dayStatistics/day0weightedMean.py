"""
Author: Fernando Collado
Github: ForFer
"""

"""
Task
Given an array, X, of N integers and an array, W, representing the respective
weights of X's elements, calculate and print the weighted mean of 's
elements. Your answer should be rounded to a scale of decimal 1 place 

Input Format

The first line contains an integer, N, denoting the number of elements in
arrays X and W.
The second line contains N space-separated integers describing the respective
elements of array X.
The third line contains N space-separated integers describing the respective
elements of array W.

Output Format

Print the weighted mean on a new line. Your answer should be rounded to a
scale of 1 decimal place

Sample Input

5
10 40 30 50 20
1 2 3 4 5

Sample Output

32.0

"""

N = int(input())
values = list(map(int,input().split()))
weights = list(map(int,input().split()))

wmean = 0
wsum = 0
for i in range(N):
    weight = weights[i]
    wmean += values[i]*weight
    wsum += weight
print("%.1f" % float(wmean/wsum))



