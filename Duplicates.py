import pandas as pd


# 1. Both colunms name and designation find the duplicates
df=pd.DataFrame({
    'name':['prasanna','suresh','praveen','praveen','suresh'],
    'designation':['data scientist','mis1','mis1','mis','mis1']
})

find_duplicates=df[
    df['name'].duplicated(keep=False) |
    df['designation'].duplicated(keep=False)
]
# print(find_duplicates)


# 2. finding rows that are duplicated based on both columns name and designation
df1=pd.DataFrame({
    'name':['prasanna','suresh','praveen','praveen','suresh'],
    'designation':['data scientist','mis1','mis1','mis','mis1']
})
# print(df1[df1.duplicated(keep=False)]) 

# 3. finding duplicates based on specific column name

df3 = pd.DataFrame({
    'category': ['ipad', 'ipad', 'iphone', 'ipad', 'ipad'],
    'shipment_number': ['S001', 'S002', 'S001', 'S001', 'S003']
})

category_name=df3[df3['category']=='ipad']

based_on_category_find_shipment_duplicates=category_name[category_name.duplicated(subset='shipment_number', keep=False)]
result=based_on_category_find_shipment_duplicates
# print(result)

# If you want rows where either col1 or col2 has duplicates, use |:
duplicates = df3[
    df3['category'].duplicated(keep=False) |
    df3['shipment_number'].duplicated(keep=False)
]

result=duplicates.drop_duplicates(inplace=True) # Remove duplicate rows from the result
print(result)