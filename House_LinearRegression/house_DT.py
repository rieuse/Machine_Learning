import pandas as pd
import numpy as np
from sklearn.learning_curve import learning_curve
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt


row_df = pd.read_csv('house_price.csv')
df = row_df[row_df.iloc[:,1] !='多']
data_X = df[['rooms','halls','size','unit_price']]
data_y = df.price


train_sizes, train_score, test_score = learning_curve(
    DecisionTreeRegressor(max_depth=16), data_X, data_y, cv=10, scoring='r2',
    train_sizes=np.linspace(0.0, 1.0, num=30)[1:])

train_score_mean = np.mean(train_score, axis=1)
test_score_mean = np.mean(test_score, axis=1)

plt.plot(train_sizes, train_score_mean, 'o-', color="r",
         label="Training")
plt.plot(train_sizes, test_score_mean, 'o-', color="g",
        label="Cross-validation")

plt.xlabel("Training examples")
plt.ylabel("Score")
plt.show()







