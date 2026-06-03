import pandas as pd

Data={
    'Name':['Tom', 'nick', 'krish', 'jack'],    
    'Age':[20, 21, 19, 18],
    'City':['New York', 'Los Angeles', 'Chicago', 'Houston']    
}
df=pd.DataFrame(Data)
# print(df.columns)
# print(df.tail(0))
# print(df.values)

df=pd.DataFrame(Data, index=['a', 'b', 'c', 'd'])
print(df)
print(df.describe())

 