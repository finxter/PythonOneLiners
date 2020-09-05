# Palindrome Python One-Liner
phrase.find(phrase[::-1])

# Swap Two Variables Python One-Liner
a, b = b, a

# Sum Over Every Other Value Python One-Liner
sum(stock_prices[::2])

# Read File Python One-Liner
[line.strip() for line in open(filename)]

# Factorial Python One-Liner
reduce(lambda x, y: x * y, range(1, n+1))

# Performance Profiling Python One-Liner
python -m cProfile foo.py

# Superset Python One-Liner
lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])

# Fibonacci Python One-Liner
lambda x: x if x<=1 else fib(x-1) + fib(x-2)

# 2. Quicksort Python One-liner
lambda L: [] if L==[] else qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])

# 1. Sieve of Eratosthenes Python One-liner
reduce( (lambda r,x: r-set(range(x**2,n,x)) if (x in r) else r), range(2,int(n**0.5)), set(range(2,n)))

