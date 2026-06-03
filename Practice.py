import pandas as pd
# Read the Excel file

df=pd.read_excel("C:\\Users\\prasa\\Downloads\\logistics.xlsx")
# Display the first few rows of the DataFrame

# print(df.sample(5)) # Displays a random sample of 5 rows from the DataFrame

Above_10000_sales=df.loc[(df['Total_Amount'] > 100000) & (df ['State'] =="Tamil Nadu")]    # Filters the DataFrame to include only rows where the 'Total_Amount' column is greater than 10000
# print(Above_10000_sales.tail(10)) # Displays the last 10 rows of the filtered DataFrame

# unique_values=df['State'].unique()# Retrieves the unique values from the 'State' column
# print(unique_values)

# print(df['State'].unique()) # Counts the occurrences of each unique value in the 'State' column and returns a Series with the counts 

# result = df[df['State'].isin(['Telangana'])] # Filters the DataFrame to include only rows where the 'State' column is either 'Tamil Nadu' or 'Kerala'
# print(result)

# columns=df.columns # Retrieves the column names of the DataFrame
# # print(columns)
# Category_st=df.sort_values(by='Category')
# print(df['Category'].sort_values()) # Retrieves the 'Category' column from the DataFrame



# 