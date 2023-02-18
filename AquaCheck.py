import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

sc=StandardScaler()
dataset = pd.read_csv("Dataset.csv")
head=[]
meanValues=[]
for heading in dataset.columns:
    head.append(heading)
for i in head:
    meanValues.append(dataset[i].mean())
for i in meanValues:
    dataset.fillna(i, inplace=True)
# dataset=sc.fit_transform(dataset)
# dataset=pd.DataFrame(dataset)
print(dataset)