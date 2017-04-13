"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/gridland-metro
"""

rows, columns, trains = list(map(int, input().split()))

grid = [[0 for _ in range(columns)] for _ in range(rows)]

for _ in range(trains):
    row, begin, end = list(map(int, input().split()))

    for i in range(begin, end):
       grid[row-1][i-1] = 1

posts = 0
for row in grid:
    posts += columns-sum(row)

print(posts)
