"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""

Singly-linked list methods

https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
"""

from node import Node

def insert_tail(head, data):
    if not head:
        return Node(data)
    else:
        current = head
        while current.next:
            current = current.next
        current.next = Node(data)

        return head


def insert_head(head, data):
    return Node(data, head)

def insert_nth(head, data, position):
    if position == 0:
        return Node(data, head)
    else:
        previous = None
        current = head
        for i in range(position):
            if i+1 == position:
                previous = current
            current = current.next

        previous.next = Node(data, current)
    return head

def delete(head, position):
    if position == 0:
        return head.next
    else:
        previous = None
        current = head
        for i in range(position):
            if i+1 == position:
                previous = current
            current = current.next

        previous.next = current.next
    return head








