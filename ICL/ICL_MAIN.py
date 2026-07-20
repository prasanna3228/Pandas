import pandas as pd
import os

# ==========================================
# FILE PATHS
# ==========================================

file_path = r"C:\Users\prasa\Downloads\logistics11.xlsx"
output_folder = r"C:\Users\prasa\Downloads\Company Pivot Files"

os.makedirs(output_folder, exist_ok=True)

# ==========================================
# READ EXCEL
# ==========================================

# Read Data sheet
df = pd.read_excel(file_path, sheet_name="Data")

# ==========================================
# CREATE COMPANY REPORTS
# ==========================================

for company, data in df.groupby("Company"):

    print(f"Creating Report : {company}")

    # ======================================
    # Get Charge Columns for Current Company
    # ======================================

    company_charge_columns = sorted(
        data["Name of the charges"]
        .dropna()
        .astype(str)
        .unique()
    )

    # ======================================
    # Create Pivot Table
    # ======================================

    pivot = pd.pivot_table(
        data,
        index=[
            "FWB",
            "Destination",
            "Psc",
            "Business type",
            "Company",
            "AWB"
        ],
        columns="Name of the charges",
        values="Net Amount",
        aggfunc="sum",
        fill_value=0
    ).reset_index()

    pivot.columns.name = None

    # ======================================
    # Fixed Columns
    # ======================================

    fixed_columns = [
        "FWB",
        "Destination",
        "Psc",
        "Business type",
        "Company",
        "AWB"
    ]

    # ======================================
    # Add Missing Charge Columns (if any)
    # ======================================

    for col in company_charge_columns:
        if col not in pivot.columns:
            pivot[col] = 0

    # Arrange Columns
    pivot = pivot[fixed_columns + company_charge_columns]

    # ======================================
    # Create File Name
    # ======================================

    company_name = str(company).strip()

    # Remove invalid filename characters
    for ch in r'<>:"/\|?*':
        company_name = company_name.replace(ch, "_")

    output_file = os.path.join(
        output_folder,
        f"{company_name}.xlsx"
    )

    # ======================================
    # Save Excel File
    # ======================================

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        pivot.to_excel(
            writer,
            sheet_name="Report",
            index=False
        )

    print(f"Saved : {company_name}.xlsx")

print("\nAll Company Files Created Successfully!")