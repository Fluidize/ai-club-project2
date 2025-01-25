import pandas as pd
data = pd.read_csv('train_chunk.csv')
data[0:1081].to_csv('train_chunk.csv', index=False)
#32851 first year