import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

dataset = pd.read_csv("Dataset.csv")
dataset.head()
head=[]
meanValues=[]
for heading in dataset.columns:
    head.append(heading)
for i in head:
    meanValues.append(dataset[i].mean())
for i in meanValues:
    dataset.fillna(i, inplace=True)

variables=[]
for i in range(len(head)-1):
    variables.append(head[i])
    plt.scatter(dataset[variables[i]],dataset['Potability'])

X = dataset[variables]
Y = dataset['Potability']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
clf = svm.SVC(kernel='rbf', C=1, gamma=0.1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)