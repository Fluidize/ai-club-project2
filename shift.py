import pandas

arr1 = [1,2,3,4]
arr2 = [1,2,3,4]

df = pandas.DataFrame(arr1 , arr2)

print(df.shift(1))