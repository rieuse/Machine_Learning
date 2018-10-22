# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")
submit = pd.read_csv("data/sample_submit.csv")
# 删除id
train.drop('CaseId', axis=1, inplace=True)
test.drop('CaseId', axis=1, inplace=True)

# 取出训练集的y
y_train = train.pop('Evaluation')


"""决策树"""
clf = KNeighborsClassifier(n_neighbors=18)
clf.fit(train, y_train)
y_pred = clf.predict_proba(test)[:, 1]

# 输出预测结果
submit['Evaluation'] = y_pred
submit.to_csv('data/KNN_prediction.csv', index=False)