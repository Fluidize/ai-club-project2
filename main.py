import sklearn
import pandas as pd
import os
import numpy

print(os.chdir(r'C:\Users\User\Documents\GitHub\ai-club-project2'))

data = pd.read_csv('train_chunk.csv')

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

X = data.drop(columns=['num_sold'],inplace=False)
X = cleanup(X, column=X.columns.tolist())
y = data['num_sold']

print(X.head())