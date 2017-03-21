"""
Author: Fernando Collado
Github: ForFer
"""

# The sole purpose of this file is to learn about:
# - Deque
# - Iterator functions
# - Decorators

from collections import deque


def deque_examples():
    d = deque()
    print("Empty deque", d)
    d = deque([1,2,3,4])
    print("Hardcoded list", d)
    d = deque(i for i in range(10))
    print("Using a generator", d)
    
    d.clear()
    for i in range(1,5):
        d.append(i)
    
    d.append(5)
    d.appendleft(0)
    print("deque after append and appendleft", d)
    print("Num. repetitions of 3: ", d.count(3))
    
    d.extend(j for j in range(7,10))
    
    print(d)
    
    d.extendleft(j for j in range(-1,-5,-1))
    print("Deque after extending", d)
    
    print("Index of number 4", d.index(4))

    print("pop", d.pop())

    print("popleft", d.popleft())
    print("deque: ", d)
    try: 
        d.remove(4)
    except:
        print("Could not remove 4, it's not there!")
    print("Index of number 4: ", d.index(0))
    print("deque: ", d)
    d.rotate(2)
    print("After rotate right: ", d)
    d.rotate(-3)
    print("Ater rotate left: ", d)

#TODO: Create an iterator (yield) function
def iterator_examples():
    pass

#TODO: Create 2/3 examples of decorators
def decorator_examples():
    pass

def Main():
    print("Some deque exmaples")
    dequeue_examples()
    iterator_examples()
    decorator_examples()
    data_structs_benchmark()

if __name__=="__Main__":
    Main()
