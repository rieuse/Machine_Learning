import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.learning_curve import learning_curve
from sklearn.metrics import r2_score
from xgboost import XGBRegressor


# https://www.lfd.uci.edu/~gohlke/pythonlibs/#xgboost

row_df = pd.read_csv('house_price.csv')
df = row_df[row_df.iloc[:,1] !='多']
data_X = df[['rooms','halls','size','unit_price']].astype('int')
data_y = df.price


train_sizes, train_score, test_score = learning_curve(
    XGBRegressor(max_depth=4), data_X, data_y, cv=10, scoring='r2',
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


# scores = []
# for i in range(1,100):
#     X_train, X_test, y_train, y_test = train_test_split(
#         data_X, data_y, test_size=0.3)
#     reg = XGBRegressor(max_depth=4, learning_rate=0.1)
#     reg.fit(X_train, y_train)
#     y_pred = reg.predict(X_test)
#     score = r2_score(y_pred, y_test)
#     scores.append(score)
# print(np.mean(scores))






