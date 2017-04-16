"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/markov-snakes-and-ladders
"""

# TODO: implement markov's chain instead of simulation

# Simulation approach
# Simulate game with each die probabilities, ladder and snakers positions 10 times, and average them

import random

t = int(input())


res = [] # To store results and print them all at the end

for _ in range(t):

    d = list(map(float, input().split(',')))
    die = [d[0]]
    # Cumulative freq
    for i in range(1,len(d)):
        die.append(die[i-1]+d[i])

    n_lad, n_sna = list(map(int, input().split(',')))

    lad = input().split()
    sna = input().split()
    up_down = {}

    for i in range(n_lad):
        temp = list(map(int, lad[i].split(',')))
        up_down[temp[0]] = temp[1]
    for i in range(n_sna):
        temp = list(map(int, sna[i].split(',')))
        up_down[temp[0]] = temp[1]

    pos = 1
    num_throws = [0 for _ in range(10)]
    reps = 0
    while reps < 10:
        throws = 0
        while pos < 100:
            print("Pos: ", pos)
            throw = random.random()
            throws += 1 
            for i in range(len(die)):
                if throw <= die[i]:
                    throw = i+1
                    break
            pos += throw
            print("New pos after throw: ", pos)
            if pos in up_down:
                print("Jumping from: ", pos, "to: ", up_down[pos])
                pos = up_down[pos]
        pos = 1
        num_throws[reps] = throws
        reps+=1

    res.append(int(sum(num_throws)/reps))

for r in res:
    print(r)


