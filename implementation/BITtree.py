#!/bin/python3

# Returns sum of arr[0..index]. This function assumes
# that the array is preprocessed and partial sums of
# array elements are stored in BITree[].
def getsum(BITTree,i):
    s = 0  #initialize result
    i = i+1
 
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s
 
# Updates a node in Binary Index Tree (BITree) at given index
# in BITree.  The given value 'val' is added to BITree[i] and
# all of its ancestors in tree.
def updatebit(BITTree , n , i ,v):
 
    i += 1
 
    while i <= n:
        BITTree[i] += v
        i += i & (-i)
 
 
def construct(arr, n):
 
    BITTree = [0]*(n+1)
 
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
   
    return BITTree

import sys

    
n = int(input("number of trees you want to make\n"))
for _ in range(n):
    a = list(map(int, input("Input numbers separated by a space for the tree\n").split()))

    print("\n\n")   
 
    BITTree = construct(a,len(a))
    print("Numbers introduced are: ",a)
    print("BITtree representation result: ", *BITTree)
    for i in range(len(BITTree)-1):
        print("Sum at",i,"is : ",getsum(BITTree,i))

    print("\n\n")
    
   
