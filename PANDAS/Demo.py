import pandas as pd
import seaborn as sns

# df=pd.DataFrame({
#     'Salary':[10000]
# })
# print(df['Salary'].astype('int'))
# print(df['Salary'].astype('float'))

# Mixed_text_and_number=pd.DataFrame({
#     "Salary":['20000','51544',234236,'prasanna']
# })
# convert_into_numeric=pd.to_numeric(Mixed_text_and_number['Salary'],errors='coerce')
# print(convert_into_numeric)
# print(Mixed_text_and_number)
# print(Mixed_text_and_number.dtypes)


print(sns.get_dataset_names())
# df=sns.load_dataset('flights')
# print(df.head())
# print(df.columns)

df=sns.load_dataset('titanic')
print(df)




