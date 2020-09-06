# Calculating the Powerset by Using Functional Programming


# Dependencies
from functools import reduce

# The Data
s = {1, 2, 3}

# The One-Liner
ps = lambda s: reduce(lambda P, x: P + [subset | {x} for subset in P], s, [set()])

# The Result
print(ps(s))
'''
[set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]
'''
