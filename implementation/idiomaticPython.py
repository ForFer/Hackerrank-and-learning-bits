"""
Author: Fernando Collado
Github: ForFer
"""

"""
Examples following the talk "Tranforming code into beautiful, idiomatic python
Source: https://www.youtube.com/watch?v=OSGv2VnC0go
"""

from time import time
import random
from functools import lru_cache
from collections import defaultdict, deque

# Machine for timings: 
# Processor: i5-2 cores
# RAM: 8GB
# OS: Ubuntu 14.04 x64

def return_always_same():
    return 10e4

@lru_cache(maxsize=None)
def return_always_same_cached():
    return 10e4

#New way of creating a new dict, defaults 0 to every value
d=defaultdict(int)
for i in range(100000):
    d[i] += 1

#DICT .items() comparative 
# Results: 
#Elapsed time for k in d:  0.010937213897705078
#Elapsed time for d.items:  0.010824441909790039
t = time()
for k in d:
    temp = k
    temp2 = d[k]
print("Elapsed time for k in d: ", time()-t)
t = time()
for k,v in d.items():
    temp = k
    temp2 = v
print("Elapsed time for d.items: ", time()-t)


print("-----------------------")
# Comparison of pop(0), insert(0) from list, to popleft, appendleft from dequeu
# Result:
# Elapsed time for pop(0), insert(0):  4.005152463912964
# Elapsed time for dequeue:  0.01324152946472168
big_list = [i for i in range(100000)]
t = time()
for i in range(50000):
    a = big_list.pop(0)
for j in range(50000):
    big_list.insert(0, j*2)
print("Elapsed time for pop(0), insert(0): ", time()-t)

big_list_2 = deque([i for i in range(100000)])
t = time()
for i in range(50000):
    a = big_list_2.popleft()
for j in range(50000):
    big_list_2.appendleft(j*2)
print("Elapsed time for dequeue: ", time()-t)

# Small check to see if the lists match
assert big_list_2.popleft() == big_list.pop(0)


print("-----------------------")
# Comparison of cached vs non-cached function
# Restuls:
# Elapsed time for non-cached function:  0.0120849609375
# Elapsed time for cached function:  0.16783380508422852
t = time()
for _ in range(100000):
    a = return_always_same()
print("Elapsed time for non-cached function: ", time()-t)

t = time()
for _ in range(100000):
    a = return_always_same_cached()
print("Elapsed time for cached function: ", time()-t)


print("-----------------------")
# String concatenation comparison + vs ''.join
# Results:
# Elapsed time for + concatenation of str:  0.037174224853515625
# Elapsed time for join concatenation of str:  0.029098987579345703
t = time()
s = ''
for i in range(100000):
    s+=str(i)
print("Elapsed time for + concatenation of str: ", time()-t)
t = time()
s = ''.join(str(i) for i in range(100000))
print("Elapsed time for join concatenation of str: ", time()-t)


month_codes = dict((fn(i+1), code)
    for i, code in enumerate('FGHJKMNQUVXZ')
    for fn in (int, str))



print("-----------------------")
# List comprehension vs generator expression (the first creates a whole new
# list, the second just iterates. The first is more costly memory-wise
# Results: 
# Elapsed time for list comprehension:  1.117339849472046
# Elapsed time for generator:  1.1601707935333252
t = time()
total = sum([num * num for num in range(1, 10000000)])
print("Elapsed time for list comprehension: ", time()-t)

t = time()
total = sum(num * num
            for num in range(1, 10000000))
print("Elapsed time for generator: ", time()-t)
