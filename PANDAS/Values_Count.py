import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"],
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai", "Mumbai", "Delhi"]
})

# print(df.value_counts())

# count city count
# print(df["City"].value_counts())

# Count unique values in the "Name" column
unique_names = df["Name"].unique()
# print(unique_names)


nunique=df["Name"].nunique()
# print(nunique)


# print(df["Name"].count())

# print(len(df))

print(df["Name"].unique())



