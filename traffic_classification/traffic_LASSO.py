# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve
from sklearn.metrics import average_precision_score

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")
submit = pd.read_csv("data/sample_submit.csv")
# 删除id
train.drop('CaseId', axis=1, inplace=True)
test.drop('CaseId', axis=1, inplace=True)

# 取出训练集的y
y_train = train.pop('Evaluation')

# train_sizes, train_score, test_score = learning_curve(
#     LogisticRegression(), train, y_train, cv=10, scoring='r2',
#     train_sizes=np.linspace(0.0, 1.0, num=30)[1:])
#
# train_score_mean = np.mean(train_score, axis=1)
# test_score_mean = np.mean(test_score, axis=1)
#
# plt.plot(train_sizes, train_score_mean, 'o-', color="r",
#          label="Training")
# plt.plot(train_sizes, test_score_mean, 'o-', color="g",
#         label="validation")
#
# plt.xlabel("Training examples")
# plt.ylabel("Score")
# plt.show()
# exit()

# 建立LASSO逻辑回归模型

clf = LogisticRegression(penalty='l1', C=1.0 ,random_state=0)
clf.fit(train, y_train)
y_pred = clf.predict_proba(test)[:, 1]

# 输出预测结果至my_LASSO_prediction.csv
submit['Evaluation'] = y_pred
submit.to_csv('data/my_LASSO_prediction.csv', index=False)