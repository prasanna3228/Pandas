import pandas as pd

# 1. Concatenation Rows (Vertical)
df1 = pd.DataFrame({
    'Name': ['John', 'Alice'],
    'Age': [25, 30]
})
df2 = pd.DataFrame({
    'Name': ['Bob', 'Emma'],
    'Age': [28, 22]})
result = pd.concat([df1, df2])
# print(result)

# 2. Concatenation Columns (Horizontal)

df1 = pd.DataFrame({'Name': ['John', 'Alice']})
df2 = pd.DataFrame({'Age': [25, 30]})
result = pd.concat([df1, df2],axis=1) 
# axis=1 join columns (side by side)
# axis=0 join rows (one after another)
# print(result)


# 3. Difference columns 
df1 = pd.DataFrame({'Name': ['John', 'Alice']})
df2 = pd.DataFrame({'City': ['New York', 'London']})
result = pd.concat([df1, df2], axis=1)
# print(result)


# 4. Missing Columns
df1 = pd.DataFrame({'Name': ['John'],'Age': [25]})
df2 = pd.DataFrame({'Name': ['Bob'],'Salary': [50000]})
result = pd.concat([df1, df2], ignore_index=True)
print(result)
