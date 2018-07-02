"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/reverse-a-linked-list
"""

from node import Node

def reverse(head):
    if not head or not head.next:
        return head

    remaining = reverse(head.next)
    head.next.next = head
    head.next = None
    return remaining


if __name__ == "__main__":
    n = Node(1)
    n2 = Node(2, n)
    n3 = Node(3, n2)
    n4 = Node(4, n3)

    _n = reverse(n)
    print("N", _n.data, _n.next.data)
