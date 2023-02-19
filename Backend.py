import pickle
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, accuracy_score, mean_squared_error
import matplotlib.pyplot as plt


df = pd.read_csv('Dataset.csv')
df.head()

fildf = df.dropna()
len(df) - len(fildf)

X = np.array(fildf.drop('Potability', axis=1))
y = np.array(fildf['Potability'])

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.03,random_state=np.random.randint(100))

model = SVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Accuracy via SVM: {accuracy_score(y_test, y_pred)}")
print(confusion_matrix(y_test, y_pred))

err = []

for i in range(1, 50):
    model = KNN(n_neighbors=i)
    model.fit(X_train, y_train)
    err.append(mean_squared_error(y_test, model.predict(X_test)))

plt.figure(figsize=(10,6))
plt.plot(range(1,50), err, color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()
print(f"Optimate value of K according to this is {err.index(min(err))}")

model = KNN(n_neighbors=err.index(min(err))+1)
model.fit(X_train, y_train)
y_pred1 = model.predict(X_test)
mse = mean_squared_error(y_test,y_pred1)
print(f"Accuracy via KNN: {accuracy_score(y_test, y_pred1)}")
print("Mean Square Error:", mse)
# print(confusion_matrix(y_test, y_pred1))
#Hello
# pickle.dump(model,open('AquaCheckModel.pkl','wb'))
