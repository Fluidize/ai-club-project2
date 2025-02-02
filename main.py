"""import pandas as pd

traindf = pd.read_csv("train.csv")
#print(traindf.head)

X=traindf.drop(["num_sold"],inplace=False,axis=1)
y=traindf["num_sold"]
col=X.columns.tolist()

def cleanup(X,column):
    for i in range(len(column)):
        data=X[column[i]].tolist()
    
        if (type(data[0])!=int):
            sets=set(data)
            lib={}
            count=0

            for j in sets:
                lib.update({j:count})
                count+=1
        
            for k in range(len(data)):
                data[k]=lib[data[k]]
            X[column[i]]=data

    return X

cleaned = cleanup(X, col)
no = open("cleantrain.txt", "w")
monkey = X.to_csv()
print(monkey.head)"""

from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import os
import numpy

data = pd.read_csv('train.csv')

def cleanup(X,column):
    for i in range(len(column)):
        data=X[column[i]].tolist()
    
        if (type(data[0])!=int):
            sets=set(data)
            lib={}
            count=0

            for j in sets:
                lib.update({j:count})
                count+=1
        
            for k in range(len(data)):
                data[k]=lib[data[k]]
            X[column[i]]=data

    return X

X = data.drop(columns=['num_sold', 'id'],inplace=False)
X = cleanup(X, column=X.columns.tolist())
y = data['num_sold'].fillna(0)

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.5)

model.fit(X_train,y_train)

yhat = model.predict(X_test)

print(mean_squared_error(y_test,yhat))