"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/counting-valleys/problem
"""



def countingValleys(n, valleys):
    current_level = 0

    total_valleys = 0

    for hill in valleys:
        if hill == "U":
            current_level += 1
            if current_level == 0:
                total_valleys += 1
        elif hill == "D":
            current_level -= 1

    return total_valleys

q = int(input())
valleys = input()
print(countingValleys(q, valleys))


        
