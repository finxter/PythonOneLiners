# Description: Python plot

## Dependencies
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data (Iris dataset)
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# One-liner
sns.pairplot(df, kind="reg")

# Result
plt.show()
