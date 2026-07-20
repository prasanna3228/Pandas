import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df=pd.read_excel("C:\\Users\\prasa\\Downloads\\logistics.xlsx")
# print(df.head()) # Displays the first few rows of the DataFrame
# print(df.columns) # Retrieves the column names of the DataFrame

Country_and_Total_amount=df.pivot_table(index='Product',columns=['Category'],values="Total_Amount",aggfunc='sum',margins=True,margins_name="Total") # Creates a pivot table that summarizes the total amount for each product and category, with margins (totals) included
# print(Country_and_Total_amount) # Displays the pivot table showing the total amount for each country
print(Country_and_Total_amount.reset_index().to_markdown(index=False))