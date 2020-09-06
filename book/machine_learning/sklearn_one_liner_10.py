# Classification with Random Forests in One Line


## Dependencies
import numpy as np
from sklearn.ensemble import RandomForestClassifier

## Data: student scores in (math, language, creativity) --> study field
X = np.array([[9, 5, 6, "computer science"],
              [5, 1, 5, "computer science"],
              [8, 8, 8, "computer science"],
              [1, 10, 7, "literature"],
              [1, 8, 1, "literature"],
              [5, 7, 9, "art"],
              [1, 1, 6, "art"]])

## One-liner
Forest = RandomForestClassifier(n_estimators=10).fit(X[:,:-1], X[:,-1])

## Result
students = Forest.predict([[8, 6, 5],
                           [3, 7, 9],
                           [2, 2, 1]])
print(students)
'''
['computer science' 'art' 'literature']
'''
