"""
Author: Fernando Collado
Github: ForFer
"""

"""
Task
The interquartile range of an array is the difference between its first (Q1) and
third (Q3) quartiles.

Given an array, X, of integers and an array, F, representing the respective
frequencies of X's elements, construct a data set, S, where each xi occurs at
frequency f. Then calculate and print S's interquartile range, rounded to a
scale of decimal place.

Tip: Be careful to not use integer division when averaging the middle two
elements for a data set with an even number of elements, and be sure to not
include the median in your upper and lower data sets.

Input Format

The first line contains an integer, , denoting the number of elements in
arrays X and F.
The second line contains space-separated integers describing the respective
elements of array X.
The third line contains space-separated integers describing the respective
elements of array F.

Output Format

Print the interquartile range for the expanded data set on a new line.
Round your answer to a scale of 1 decimal place.

Sample Input

6
6 12 8 10 20 16
5 4 3 2 1 5

Sample Output

9.0

"""
def calculateQuartile(array):
    q = -1
    if(len(array)%2!=0):
        q = array[len(array)//2]
    else:
        q = ( array[len(array)//2-1] + array[len(array)//2] ) / 2
    return q



n = int(input())
temp = list(map(int,input().split()))
freqs = list(map(int,input().split()))
values = []
for i in range(n):
    for _ in range(freqs[i]):
        values.append(temp[i])

values = sorted(values)
n = len(values)
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

print("%.1f" % float(Q[2]-Q[0]))
