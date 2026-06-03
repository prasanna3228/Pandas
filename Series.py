import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])
# print(s[2])

S1 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(S1)
print(S1['e'])
print(S1.shape)
print(S1.dtypes)
print(S1.index)
print(S1.values)    
print(S1.describe()) # Provides summary statistics of the Series    
print("Mean:",  S1.mean())
print("Median:", S1.median())
print("Standard Deviation:", S1.std()) # Provides the standard deviation of the Series
print("Sum:", S1.sum())
print("Minimum:", S1.min()) # Provides the minimum value in the Series
print("Maximum:", S1.max()) # Provides the maximum value in the Series
print("Value Counts:", S1.value_counts()) # Provides the count of unique values in the Series
print("Unique Values:", S1.unique()) # Provides the unique values in the Series
print("Number of Unique Values:", S1.nunique()) # Provides the number of unique values in the Series
print("Null Values:", S1.isnull()) # Checks for null values in the Series and returns a boolean Series indicating which values are null
print("Non-Null Values:", S1.notnull()) # Checks for non-null values
print("First 5 Values:", S1.head()) # Displays the first 5 values of the Series
print("Last 5 Values:", S1.tail()) # Displays the last 5 values of the Series
print("Sorted Values:", S1.sort_values()) # Sorts the Series by values
print("Sorted by Index:", S1.sort_index()) # Sorts the Series by index
print("Doubled Values:", S1.apply(lambda x: x * 2)) # Applies a function to each element in the Series
print("Doubled Values (Map):", S1.map(lambda x: x * 2)) # Similar to apply but used for element-wise transformations    
print("Squared Values:", S1.apply(lambda x: x ** 2)) # Applies a function to each element in the Series to calculate squared values 
print("Squared Values (Map):", S1.map(lambda x: x ** 2))
print("Values > 25:", S1.apply(lambda x: x > 25)) # Applies a function to each element in the Series to check if values are greater than 25
print("Values > 25 (Map):", S1.map(lambda x: x > 25)) # Similar to apply but used for element-wise transformations to check if values are greater than 25
print("Even Values:", S1.apply(lambda x: x % 2 == 0)) # Applies a function to each element in the Series to check if values are even
print("Even Values (Map):", S1.map(lambda x: x % 2 == 0)) # Similar to apply but used for element-wise transformations to check if values are even
print("Count of Even Values:", S1.apply(lambda x: x % 2 == 0).sum()) # Applies a function to each element in the Series to check if values are even and then sums the boolean values to get the count of even values



