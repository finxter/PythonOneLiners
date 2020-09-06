# K-Nearest Neighbors in One Line


## Dependencies
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

## Data (House Size (square meters) / House Price ($))
X = np.array([[35, 30000], [45, 45000], [40, 50000],
              [35, 35000], [25, 32500], [40, 40000]])

## One-liner
KNN = KNeighborsRegressor(n_neighbors=3).fit(X[:,0].reshape(-1,1), X[:,1])

## Result & puzzle
res = KNN.predict([[30]])
print(res)
'''
[32500.]
'''
