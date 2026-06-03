import pandas as pd

# Read the Excel file
file_path = r"C:\Users\prasa\Downloads\logistics11.xlsx"
df = pd.read_excel(file_path)

# Display basic information
# print("Dataset shape:", df.shape)
# print("\nFirst few rows:")
# print(df.head())

# print("\nColumn names:")
# print(df.columns.tolist())

# print("\nData types:")
# print(df.dtypes)

# print("\nDataset info:")
# print(df.info())

All_Columns = df.columns.tolist()
print("All Columns:", All_Columns)