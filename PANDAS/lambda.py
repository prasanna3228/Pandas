import pandas as pd
s=pd.Series([1, 2, 3, 4, 5])
# 1. Lambda Function to Square Each Element in a Series
squared = s.apply(lambda x: x**2)
# print(squared)

df = pd.DataFrame({
    'salary': [50000, 60000, 55000]
})
# 2. Lambda Function to Calculate Tax (Assuming a Tax Rate of 20%)
df['tax'] = df['salary'].apply(lambda x: x * 0.18)
df['Bonus']=df['salary'].apply(lambda x: x * 0.15)
print(df)
