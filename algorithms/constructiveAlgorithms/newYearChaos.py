"""
Author: Fernando Collado
Github: ForFer
"""

"""
It's New Year's Day and everyone's in line for the Wonderland rollercoaster
ride!

There are people queued up, and each person wears a sticker indicating
their initial position in the queue

Any person in the queue can bribe the person directly in front of them to swap
positions. If two people swap positions, they still wear the same sticker
denoting their original place in line. One person can bribe at most two
other persons.

That is to say, if n=8 and Person=5 bribes Person=4, the queue will look like
this: 1,2,3,5,4,6,7,8.

Fascinated by this chaotic queue, you decide you must know the minimum
number of bribes that took place to get the queue into its current state!

Note: Each Person X wears sticker X, meaning they were initially the Xth person in queue.

Input Format

The first line contains an integer, T, denoting the number of test cases.
Each test case is comprised of two lines; the first line has (an integer
indicating the number of people in the queue), and the second line has
space-separated integers describing the final state of the queue.

Output Format

Print an integer denoting the minimum number of bribes needed to get the
queue into its final state; print Too chaotic if the state is invalid
(requires Person X to bribe more than 2 people).

Sample Input

2
5
2 1 5 3 4
5
2 5 1 3 4

Sample Output

3
Too chaotic

"""

cycles = int(input())
movements = []

for _ in range(cycles):
    n = int(input())
    q = list(map(int,input().split()))    
    too = False
    for i in range(n):
        if (q[i]>i+3):
            too = True

    if(too):
        movements.append("Too chaotic")
    else:
        moves = 0
        for k in range(n-1):
            flag = 0
            for i in range(n-k-1):
                if(q[i]>q[i+1]):
                    temp = q[i+1]
                    q[i+1] = q[i]
                    q[i] = temp 
                    flag=1
                    moves+=1
            if(flag==0):
                break
            
        movements.append(moves)

for move in movements:
    print(move)



