"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
"""

from node import Node

def print_list(head):
    current = head
    while current:
        print(current.data)
        current = current.next


def reverse_print(head):
    if head:
        reverse_print(head.next)
        print(head.data)


def test():
    n = Node(0)
    
    n_list = [n]

    for i in range(1, 10):
        temp = Node(i)
        n_list[i-1].next = temp
        n_list.append(temp)

    reverse_print(n)

if __name__ == "__main__":
    test()
