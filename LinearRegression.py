import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#%matplotlib inline

dataset = pd.read_csv("Dataset.csv")
dataset.head()
clf = LinearRegression()
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

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2)
clf.fit(X_train,y_train)
clf.predict(X_test)
print(clf.score(X_test,y_test))