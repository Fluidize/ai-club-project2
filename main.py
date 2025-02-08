import random as rand
import pandas as pd
from sklearn.neural_network import MLPRegressor
import numpy as np
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import StandardScaler

traindf=pd.read_csv("train.csv",index_col=0)

X=traindf.drop(["num_sold"],inplace=False,axis=1)
y=traindf["num_sold"]
y = y.fillna(0)
cols=X.columns.tolist()

def cleanup(X,column):
    for i in range(len(column)):
        data=X[column[i]].tolist()

        print(i)

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

X=cleanup(X,cols)
print(X.head)

array=[984,13]
MLP=MLPRegressor()
print(array)

MLP.fit(X, y)

testdf=pd.read_csv("test.csv",index_col=0)
Xtest=testdf
testcols=Xtest.columns.tolist()

Xtest=cleanup(Xtest,testcols)

print("hear")

prediction=pd.DataFrame(MLP.predict(Xtest), columns = ["num_sold"])



prediction.index.name = "id"

prediction.index+=230130

prediction.to_csv("Prediction.csv")