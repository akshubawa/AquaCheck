import pandas as pd
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

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
minmax = MinMaxScaler()
sc = StandardScaler()

# x = pd.DataFrame(sc.fit_transform(X))
x = pd.DataFrame(minmax.fit_transform(X))

Y = dataset['Potability']

X_train, X_test, y_train, y_test = train_test_split(x, Y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
# clf = svm.SVC(kernel='rbf', C=1, gamma=0.1)
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(accuracy)