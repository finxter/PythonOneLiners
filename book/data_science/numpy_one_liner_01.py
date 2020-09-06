# Basic Two-Dimensional Array Arithmetic


## Dependencies
import numpy as np

## Data: yearly salary in ($1000) [2017, 2018, 2019]
alice = [99, 101, 103]
bob = [110, 108, 105]
tim = [90, 88, 85]
salaries = np.array([alice, bob, tim])
taxation = np.array([[0.2, 0.25, 0.22],
                     [0.4, 0.5, 0.5],
                     [0.1, 0.2, 0.1]])

## One-liner
max_income = np.max(salaries - salaries * taxation)

## Result
print(max_income)
'''
81.0
'''
