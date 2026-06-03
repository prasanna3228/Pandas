import pandas as pd
df= pd.DataFrame({
    'name':["prasanna", "praveen", "prashanth"]
    })

#Adding a new columns to the dataframe
df['age']=[20, 30, 40]
df['salary']=[50000, 60000, 70000]
#Updating the values in the 'discount' column
df['discount'] = df['salary'] * 0.1
# print(df)

#Updating the value of a specific cell
df.at[1, 'salary'] = 65000
df.loc[0, 'name'] = "prasanna kumar"

#condition based update
df.loc[df['salary'] > 60000, 'discount'] = df['salary'] * 0.2


#Deleting a column
df.drop('discount', axis=1, inplace=True)


# Delete row with index 1 // Delete row and reset index
df = df.drop(1).reset_index(drop=True)


# Delete row using a condition
df = df[df['salary'] <= 60000].reset_index(drop=True)
print(df)
