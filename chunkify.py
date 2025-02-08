import pandas as pd
import os
print(os.chdir(r'C:\Users\User\Documents\GitHub\ai-club-project2'))
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
slice_idx = 38251
train[0:slice_idx].to_csv('train_chunk.csv', index=False)
test[0:slice_idx].to_csv('test_chunk.csv', index=False)
#32851 first year