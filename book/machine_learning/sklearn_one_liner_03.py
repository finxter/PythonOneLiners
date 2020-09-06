# K-Means Clustering in One Line


## Dependencies
from sklearn.cluster import KMeans
import numpy as np

## Data (Work (h) / Salary ($))
X = np.array([[35, 7000], [45, 6900], [70, 7100],
              [20, 2000], [25, 2200], [15, 1800]])

## One-liner
kmeans = KMeans(n_clusters=2).fit(X)

## Result & puzzle
cc = kmeans.cluster_centers_
print(cc)
'''
[[  20. 2000.]
 [  50. 7000.]]
'''
