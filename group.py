from sklearn.preprocessing import StandardScaler

scaler=StandardScaler(with_mean=False)

chunks=np.array_split(Xtest, 29)

#step 1 split the data into 29 chunks
#step 2 form a prediction for the first chunk output to csv
(scaler.fit(chunks[0]))
(scaler.transform(chunks[0]))

predictions=[]
for i in range(len(chunks)):
    run=scaler.fit_transform(chunks[i])
    """run=scaler.transform(chunks[i])"""
    results=pd.DataFrame(reg.predict(run),columns=["sales"])
    predictions.append(results)