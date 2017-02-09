"""
Author: Fernando Collado
Github: ForFer
"""

"""
We define a modified Fibonacci sequence using the following definition:

    Given terms ti and ti+1 where i € [1,inf) , term ti+2 is computed using the following relation:

    ti+2 = ti + (ti+1)²

For example, if term t1=0 and t2=1, term t3=0+1²=1 , term t4=1+1²=2, term
t5=1+2²=5, and so on.

Given three integers, t1, t2, and n, compute and print term tn of a modified
Fibonacci sequence.

Note: The value of tn may far exceed the range of a 64-bit integer. Many
submission languages have libraries that can handle such large results but, for
those that don't (e.g., C++), you will need to be more creative in your
solution to compensate for the limitations of your chosen submission language.

Input Format

A single line of three space-separated integers describing the respective
values of t1, t2, and n.

Output Format

Print a single integer denoting the value of term tn in the modified Fibonacci
sequence where the first two terms are t1 and t2.

Sample Input

0 1 5

Sample Output

5

"""
 
def calcFib (t1,t2, n):
    seq = [0 for _ in range(n)]
    seq[0] = t1
    seq[1] = t2
    for i in range(2, n):
        seq[i] = seq[i-2] + seq[i-1]**2 
    return seq[n-1]

def Main():
    t1,t2,n, = map(int,input().split())
    
    print(calcFib(t1,t2,n))

if __name__=="__main__":
    Main()

