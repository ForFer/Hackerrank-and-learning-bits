"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/apple-and-orange
"""

start_pos,end_pos = list(map(int, input().split()))
apple_tree,orange_tree = list(map(int, input().split()))
apples,oranges = list(map(int, input().split()))
apples_coordinates = list(map(int, input().split()))
oranges_coordinates = list(map(int, input().split()))

total_apples = 0
total_oranges = 0
for apple in apples_coordinates:
    apple_pos = apple_tree + apple
    if apple_pos <= end_pos and apple_pos >= start_pos:
        total_apples += 1
for orange in oranges_coordinates:
    orange_pos = orange_tree + orange
    if orange_pos <= end_pos and orange_pos >= start_pos:
        total_oranges += 1

print(total_apples)
print(total_oranges)
