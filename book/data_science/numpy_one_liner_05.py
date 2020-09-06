# Broadcasting, Slice Assignment, and Reshaping to Clean Every i-th Array Element


## Dependencies
import numpy as np

## Sensor data (Mo, Tu, We, Th, Fr, Sa, Su)
tmp = np.array([1, 2, 3, 4, 3, 4, 4,
                5, 3, 3, 4, 3, 4, 6,
                6, 5, 5, 5, 4, 5, 5])

## One-liner
tmp[6::7] = np.average(tmp.reshape((-1,7)), axis=1)

## Result
print(tmp)
'''
[1 2 3 4 3 4 3 5 3 3 4 3 4 4 6 5 5 5 4 5 5]
'''
