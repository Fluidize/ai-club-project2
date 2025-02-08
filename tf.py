from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import os
import numpy
import pickle
import tensorflow as tf
import keras

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
data.drop(['id'],axis=1, inplace=True)

X = data.drop(columns=['num_sold'],inplace=False)
X = cleanup(X, column=X.columns.tolist())
y = data['num_sold'].fillna(0)

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.5)


loss_fn = tf.keras.losses.MeanSquaredError()
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(4,)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])
model.fit(X_train,y_train, epochs=10)

yhat = model.predict(X_test)

print(y_test.head)

print(mean_squared_error(y_test,yhat))

if input('y/n ') == 'y':
    with open('model.pkl', 'wb') as file:
        pickle.dump(model, file)