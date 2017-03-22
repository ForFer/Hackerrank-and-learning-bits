"""
Author: Fernando Collado
Github: ForFer
"""

"""
Task
Given an array, X, of N integers, calculate and print the the respective mean,
median, and mode on separate lines. If your array contains more than one
modal value, choose the numerically smallest one.

Input Format

The first line contains an integer, N, denoting the number of elements in the
array.
The second line contains N space-separated integers describing the array's
elements.

Output Format

Print lines of output in the following order:

    Print the mean on a new line, to a scale of 1 decimal place
    Print the median on a new line, to a scale of 1 decimal place 
    Print the mode on a new line; if more than one such value exists, print the
numerically smallest one.

Sample Input

10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Sample Output

43900.6
44627.5
4978
"""
import statistics as stats


N = int(input())
values = list(map(int,input().split()))

print("%.1f" % stats.mean(values))
print("%.1f" % stats.median(values))

try:
    print(stats.mode(values))
except:
    d = {}
    for i in values:
        if(i in d):
            d[i] += 1
        else:
            d[i] = 1
    mode = max(d.values())
    if(mode != 1):
        print(list(d.keys())[list(d.values()).index(mode)])
    else:
        print(min(values))
