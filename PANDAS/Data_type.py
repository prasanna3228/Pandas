import pandas as pd

df=pd.DataFrame({
    'age':['25', '30', '35', '40'],
})
print(df.dtypes)
df['age']=df['age'].astype('int') # Converts the 'age' column in the DataFrame to integer data type
print(df.dtypes)


# Handling conversion error
df1=pd.DataFrame({
    'age':['25', '30', 'thirty-five', '40']
    })
df1['age']=pd.to_numeric(df1['age'], errors='coerce') # Converts the 'age' column in the DataFrame to numeric data type, coercing errors to NaN     
print(df1.dtypes)




