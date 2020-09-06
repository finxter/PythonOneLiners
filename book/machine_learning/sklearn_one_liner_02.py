# Logistic Regression in One Line
from sklearn.linear_model import LogisticRegression
import numpy as np

## Data (#cigarettes, cancer)
X = np.array([[0, "No"],
              [10, "No"],
              [60, "Yes"],
              [90, "Yes"]])

## One-liner
model = LogisticRegression().fit(X[:,0].reshape(-1,1), X[:,1])

## Result & puzzle
print(model.predict([[2],[12],[13],[40],[90]]))
'''
['No' 'No' 'Yes' 'Yes' 'Yes']
'''
