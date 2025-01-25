import sklearn
import pandas as pd
import os
import numpy

print(os.chdir(r'C:\Users\User\Documents\GitHub\ai-club-project2'))

data = pd.read_csv('train_chunk.csv')

def getDaySales(df):
    sales = []
    for x in df.index:
        tarr = []
        for y in range(90):
            for row in data['num_sold'].to_list():
                tarr.append(row)
        tarr.append(sales)
    return sales

print(getDaySales(data))