from sklearn import datasets, tree
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, average_precision_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


iris = datasets.load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)


clf = LogisticRegression(penalty='l1', C=1.0 ,random_state=0)
clf.fit(x_train, y_train)
y_pred = clf.predict_proba(x_test)[:, 1]

print(average_precision_score(y_test,y_pred))