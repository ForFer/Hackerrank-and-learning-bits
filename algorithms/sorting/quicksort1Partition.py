"""
Author: Fernando Collado
Github: ForFer
"""

"""
The previous challenges covered Insertion Sort, which is a simple and intuitive
sorting algorithm with an average case performance of O(n²). In these next few
challenges, we're covering a divide-and-conquer algorithm called Quicksort (also
known as Partition Sort).

Step 1: Divide
Choose some pivot element, , and partition your unsorted array, ar, into three
smaller arrays: left, right, and equal, where each element in left<p, each
element in right>p, and each element in equal = p.

Challenge
Given ar and p=ar[0], partition ar into left, right, and equal using the Divide instructions above. Then
print each element in left followed by each element in equal, followed by each
element in right on a single line. Your output should be space-separated.

Input Format

The first line contains n (the size of ).
The second line contains n space-separated integers describing ar (the unsorted
array). The first integer (corresponding to ar[0]) is your pivot element, p.

Output Format

On a single line, print the partitioned numbers (i.e.: the elements in left, then
the elements in equal, and then the elements in right). Each integer should be separated
by a single space.

Sample Input

5
4 5 3 7 2

Sample Output

3 2 4 5 7

"""

n = int(input())
ar = list(map(int, input().split()))

left = []
equal = []
right = []

p = ar[0]
for i in ar:
    if i < p:
        left.insert(0,i)
    elif i>p:
        right.append(i)
    else:
        equal.append(i)
arr = left + equal + right
print(' '.join(map(str,arr)))


