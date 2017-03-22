"""
Author: Fernando Collado
Github: ForFer
"""

"""
Enter-View (EV) is a linear, street-like country. By linear, we mean all the cities
of the country are placed on a single straight line - the x-axis. Thus every
city's position can be defined by a single coordinate, xi, the distance from the
left borderline of the country. You can treat all cities as single points.

Unfortunately, the dictator of telecommunication of EV (Mr. S. Treat Jr.)
doesn't know anything about the modern telecom technologies, except for
peer-to-peer connections. Even worse, his thoughts on peer-to-peer connections
are extremely faulty: he believes that, if Pi people are living in city i, there
must be at least Pi cables from city i to every other city of EV - this way he can
guarantee no congestion will ever occur!

Mr. Treat hires you to find out how much cable they need to implement this
telecommunication system, given the coordination of the cities and their
respective population.

Note that The connections between the cities can be shared. Look at the example
for the detailed explanation.

Input Format

A number T is given in the first line and then comes T blocks, each representing a
scenario.

Each scenario consists of three lines. The first line indicates the number of
cities (N). The second line indicates the coordinates of the N cities. The third
line contains the population of each of the cities. The cities needn't be in
increasing order in the input.

Output Format

For each scenario of the input, write the length of cable needed in a single
line modulo 1,000,000,007.


Border to border length of the country

Sample Input

2  
3  
1 3 6  
10 20 30  
5  
5 55 555 55555 555555  
3333 333 333 33 35

Sample Output

280  
463055586
"""


#Source of this BIT (fenwick)
#https://www.quora.com/Algorithms/How-can-I-efficiently-compute-the-number-of-swaps-required-by-slow-sorting-methods-like-insertion-sort-and-bubble-sort-to-sort-a-given-array/answer/Yoshiya-Miyata?srid=3BFg&share=1
class Bit:
    def __init__(self, n):
        sz = 1
        while n > sz:
            sz *= 2
        self.size =sz
        self.data = [0]*sz
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):
        while i < self.size:
            self.data[i] += x
            i += i & -i




n = int(input())

cables = []
for _ in range(n):
    cities = int(input())
    coordinates = list(map(int,input().split()))
    population = list(map(int,input().split()))

    cable = 0 
    visited = set()
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i!=j and (j,i) not in visited:
                dis = coordinates[j]-coordinates[i]
                visited.add((i,j))
                cable += dis * max(population[i], population[j])
    cables.append(cable%1000000007)

for c in cables:
    print(c)
                
                
