"""
Author: Fernando Collado
Github: ForFer
"""

"""
In Insertion Sort Part 1, you sorted one element into an array. Using the same
approach repeatedly, can you sort an entire unsorted array?

Guideline: You already can place an element into a sorted array. How can you
use that code to build up a sorted array, one element at a time? Note that in
the first step, when you consider an array with just the first element - that
is already "sorted" since there's nothing to its left that is smaller.

In this challenge, don't print every time you move an element. Instead,
print the array after each iteration of the insertion-sort, i.e., whenever the
next element is placed at its correct position.

Since the array composed of just the first element is already "sorted",
begin printing from the second element and on.

Input Format
There will be two lines of input:

    s- the size of the array
    arr- a list of numbers that makes up the array

Output Format
On each line, output the entire array at every iteration.

Sample Input

6
1 4 3 5 6 2

Sample Output

1 4 3 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 2 3 4 5 6 

"""

def printArr(arr):
    s = ''
    for a in arr:
        s += str(a) + " "
    print(s)

n = int(input())
arr = list(map(int,input().split()))

for j in range(n):
    e = arr[j]
    k = j
    while k>0 and e < arr[k-1] :
        arr[k] = arr[k-1]
        k-=1
    arr[k] = e
    if j != 0 :        
        printArr(arr)
