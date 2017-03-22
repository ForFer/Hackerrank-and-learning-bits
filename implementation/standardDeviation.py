"""
Author: Fernando Collado
Github: ForFer
"""

"""
Task
Given an array, X, of N integers, calculate and print the standard deviation. Your
answer should be in decimal form, rounded to a scale of 1 decimal place. An
error margin of +-0.1 will be tolerated for the standard deviation.

Input Format

The first line contains an integer, N, denoting the number of elements in the
array.
The second line contains N space-separated integers describing the respective
elements of the array.

Output Format

Print the standard deviation on a new line, rounded to a scale of decimal
place (i.e., format).

Sample Input

5
10 40 30 50 20

Sample Output

14.1

"""
import statistics as stats
import math

n = int(input())
values = list(map(int,input().split()))

mean = stats.mean(values)

stddev = math.sqrt( (sum( [(x-mean)**2 for x in values] ) /n ) )

print("%.1f" % stddev)
