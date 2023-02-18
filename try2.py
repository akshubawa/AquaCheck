import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.svm import SVC

sc=StandardScaler()
dataset = pd.read_csv("Dataset.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
dataset.head()

head=[]
meanValues=[]
for heading in dataset.columns:
    head.append(heading)
for i in head:
    meanValues.append(dataset[i].mean())
for i in meanValues:
    dataset.fillna(i, inplace=True)

scaler = StandardScaler()
X = scaler.fit_transform(X)
min_max_scaler = MinMaxScaler()
X = min_max_scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

accuracy = svm.score(X_test, y_test)
print('Accuracy:', accuracy)