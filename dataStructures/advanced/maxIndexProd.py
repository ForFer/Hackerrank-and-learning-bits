"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/find-maximum-index-product
"""

# naive approach -> O(n^2)
# All cases with correct solutions, but 0,5,11, and 12 termianted due to timeout
def naive_approach(a):
    max_index_product = 0 

    for i in range(n):
        ai = a[i]
        left = 0
        right = 0
        if i!=0 and i!=n-1:
            for k in range(i,-1, -1):
                if a[k] > ai: 
                    left = k+1 
                    break
            for k in range(i, n): 
                if a[k] > ai: 
                    right = k+1 
                    break
        index_product = left*right
        if index_product > max_index_product:
            max_index_product = index_product
    return max_index_product

# TODO: use stack or left/right arrays to keep tabs
def tabs_approach(a, n):
    pass

n = int(input())
a = list(map(int, input().split()))

print(naive_approach(a))
print(tabs_approach(a, n))
