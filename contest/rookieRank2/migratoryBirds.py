"""
Author:Fernando Collado
Github: ForFer
"""

"""
A flock of birds is flying across the continent. Each bird has a type, and the
different types are designated by the ID numbers 1, 2, 3, 4, and 5.

Given an array of integers where each integer describes the type of a bird in
the flock, find and print the type number of the most common bird. If two or
more types of birds are equally common, choose the type with the smallest ID
number.

Input Format

The first line contains an integer denoting n (the number of birds).
The second line contains n space-separated integers describing the respective type
numbers of each bird in the flock.

Output Format

Print the type number of the most common bird; if two or more types of birds are
equally common, choose the type with the smallest ID number.

Sample Input 0

6
1 4 4 4 5 3

Sample Output 0

4

"""
import operator

n = int(input())

birds = list(map(int, input().split()))

types = {1:0,2:0,3:0,4:0,5:0}

for bird in birds:
    types[bird]+=1

sorted_types = sorted(types.items(), key=operator.itemgetter(1), reverse=True)

m = max(types.items(), key=operator.itemgetter(1))

if sorted_types[1][1] == m[1]:
    minType = 0
    for i in sorted_types:
        if sorted_types[i] < minType:
            minType = i

    print(minType)
else:
    print(m[0])

