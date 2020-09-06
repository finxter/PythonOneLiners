# Finding Prime Numbers with the Sieve of Eratosthenes


## Dependencies
from functools import reduce

## The Data
n = 100

## The One-Liner
primes = reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r, range(2, int(n**0.5) + 1), set(range(2, n)))

## The Result
print(primes)
'''
{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
'''
