# Basic Statistics in One Line


## Dependencies
import numpy as np

## Stock Price Data: 5 companies
# (row=[price_day_1, price_day_2, ...])
x = np.array([[8, 9, 11, 12],
              [1, 2, 2, 1],
              [2, 8, 9, 9],
              [9, 6, 6, 3],
              [3, 3, 3, 3]])

## One-liner
avg, var, std = np.average(x, axis=1), np.var(x, axis=1), np.std(x, axis=1)

## Result & puzzle
print("Averages: " + str(avg))
print("Variances: " + str(var))
print("Standard Deviations: " + str(std))
'''
Averages: [10.   1.5  7.   6.   3. ]
Variances: [2.5  0.25 8.5  4.5  0.  ]
Standard Deviations: [1.58113883 0.5        2.91547595 2.12132034 0.        ]
'''
