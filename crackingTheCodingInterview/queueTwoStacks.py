"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem
"""

"""
Two solutions implemented, following hrank format, creating a queue class, and
the pythonic way, using deque data structure from collections
"""

# First way, hrank format
class MyQueue(object):

    def __init__(self):
        self.main_stack = []
        self.aux_stack = []

    def peek(self):
        if not self.aux_stack:
            while self.main_stack:
                self.aux_stack.append(self.main_stack.pop())

        value = self.aux_stack.pop()
        self.aux_stack.append(value)
        return value
        
    def pop(self):
        # for pure stack behaviour, list comprehension has been avoided
        if not self.aux_stack:
            while self.main_stack:
                self.aux_stack.append(self.main_stack.pop())
        return self.aux_stack.pop()
        
    def put(self, value):
        self.main_stack.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())


# Second solution, using deque
# Fast solution, using python data structure deque, a list with pointers to both
# head and tail, so that pop and pop(0) (among others) are O(1), and it actually
# works exactly like a queue formed by 2 stacks

# from collections import deque

# q = int(input())

# d = deque()

# for _ in range(q):
#    data = list(map(int, input().split()))

#    if data[0] == 1:
#        d.append(data[1])        
#    elif data[0] == 2:
#        trash = d.popleft()
#    else:
#        print(d[0])
