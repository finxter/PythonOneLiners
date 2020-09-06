# Counting Permutations with Recursive Factorial Functions


## The Data
n = 5

## The One-Liner
factorial = lambda n: n * factorial(n-1) if n > 1 else 1

## The Result
print(factorial(n))
'''
120
'''
