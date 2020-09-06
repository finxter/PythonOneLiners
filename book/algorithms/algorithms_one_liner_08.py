# Calculating the Fibonacci Series with the reduce() Function


# Dependencies
from functools import reduce

# The Data
n = 10

# The One-Liner
fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [0, 1])

# The Result
print(fibs)
'''
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''
