"""
Author: Fernando Collado
Github: ForFer
"""

"""
Consider an array of integers, A = a0,a1...an-1. We define the absolute difference between two
elements, ai and aj (where i!=j), to be the absolute value of |ai-aj|.

Given an array of n integers, find and print the minimum absolute difference
between any two elements in the array.

Input Format

The first line contains a single integer denoting n (the number of integers).
The second line contains space-separated integers describing the respective
values of a0, a1... an-1.

Output Format

Print the minimum absolute difference between any two elements in the array.

Sample Input 0

3
3 -7 0

Sample Output 0

3


"""

n = int(input())
values = list(map(int, input().split()))

minimun = 9223372036854775807

for i in range(len(values)):
    for j in range(i, len(values)):
        if i != j:
            if abs(values[i]-values[j]) < minimun:
                minimun = abs(values[i]-values[j])

print(minimun)
