import pandas as pd

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
                print(data[k])
            X[column[i]]=data

    return X

print("Reading")
traindf = pd.read_csv("train.csv")

print("Converting Dates")
daylist = []
monthlist = []
for i in traindf["date"]:
    daylist.append(i[5:6])
    monthlist.append(i[8:9])

print("Converting Dates")
traindf.to_csv("cleantrain.csv")