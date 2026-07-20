import pandas as pd
import os

# Read Excel file
df = pd.read_excel(r"C:\Users\prasa\Downloads\logistics11.xlsx")

# Column containing company names
company_column = "Company"

# Output folder
output_folder = r"C:\Users\prasa\Downloads\Company Files"
os.makedirs(output_folder, exist_ok=True)

# Create one Excel file for each company
for company, data in df.groupby(company_column):

    # Remove invalid filename characters
    filename = "".join(c for c in str(company) if c not in r'\/:*?"<>|')

    output_path = os.path.join(output_folder, f"{filename}.xlsx")

    data.to_excel(output_path, index=False)

print("Done!")

