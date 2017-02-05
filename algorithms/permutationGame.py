"""
Author: Fernando Collado
Github: ForFer
"""

"""
Alice and Bob play the following game:

1 .They choose a permutation of the first N numbers to begin with.
2. They play alternately and Alice plays first.
3. In a turn, they can remove any one remaining number from the permutation.
4. The game ends when the remaining numbers form an increasing sequence. The
person who played the last turn (after which the sequence becomes
increasing) wins the game.

Assuming both play optimally, who wins the game?

Input Format

The first line contains the number of test cases T.T test cases follow. Each case
contains an integer N on the first line, followed by a permutation of the
integers 1..N on the second line.

Output Format

Output T lines, one for each test case, containing "Alice" if Alice wins the game
and "Bob" otherwise.

Sample Input

2
3
1 3 2
5
5 3 2 1 4

Sample Output

Alice
Bob

"""
