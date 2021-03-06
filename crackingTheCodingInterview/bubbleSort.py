"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-bubble-sort
"""

# Same as implementation/20-sorting.py

def bubbleSort(arr):
    swaps = 0 
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                swaps+=1
        if swaps==0:
            break
    
    return swaps, arr[0], arr[len(arr)-1]


n = int(input().strip())
a = [int(a_temp) for a_temp in input().split()]


swaps, first, last = bubbleSort(a)
print("Array is sorted in %d swaps." % swaps)
print("First Element:", first)
print("Last Element:", last)

