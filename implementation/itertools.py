"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/itertools-product/problem
"""

def product():
    from itertools import product
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(*list(product(a,b)))


def permutations():
    from itertools import permutations
    s, n = input().split()

    for permutation in list(permutations(sorted(s), int(n))):
        print(''.join(permutation))


def combinations():
    from itertools import combinations
    s, n = input().split()
    s = sorted(s)

    for i in range(1, int(n)+1):
        print('\n'.join([''.join(combination) for combination in combinations(s, i)]))


def groupby():
    from itertools import groupby
    s = input()
    print(*[(len(list(g)), int(k)) for k,g in groupby(s)])


def iterable():
    from itertools import combinations

    n = int(input())
    s = input().split()
    k = int(input())

    combinations = list(combinations(s, k))
    probability = list(filter(lambda c:'a' in c, combinations))
    print("{0:.3}".format(len(probability)/len(combinations)))



def main():
    #product()
    #permutations()
    #combinations()
    #groupby()
    iterable()

if __name__ == "__main__":
    main()
