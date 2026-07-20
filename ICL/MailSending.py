import pandas as pd
import os
import win32com.client as win32


# ==========================================
# FILE PATHS
# ==========================================

file_path = r"C:\Users\prasa\Downloads\logistics11.xlsx"

output_folder = r"C:\Users\prasa\Downloads\Company Pivot Files"


# ==========================================
# READ MAIL MASTER
# ==========================================

mail_df = pd.read_excel(
    file_path,
    sheet_name="Mail_Master"
)


# ==========================================
# OPEN OUTLOOK
# ==========================================

outlook = win32.Dispatch("Outlook.Application")


# ==========================================
# SEND MAILS DYNAMICALLY
# ==========================================

for _, row in mail_df.iterrows():

    company = str(row["Company"]).strip()


    # Find company file

    attachment = os.path.join(
        output_folder,
        f"{company}.xlsx"
    )


    # Skip if file not available

    if not os.path.exists(attachment):

        print(
            f"Skipping {company} - File not found"
        )

        continue


    # Create mail

    mail = outlook.CreateItem(0)


    mail.To = str(row["To"])

    mail.CC = str(row["CC"])

    mail.Subject = str(row["Subject"])

    mail.Body = str(row["Body"])


    # Attach file

    mail.Attachments.Add(
        attachment
    )


    # Display email

    mail.Display()


    # For automatic sending:
    # mail.Send()


    print(
        f"Mail Prepared : {company}"
    )


print("Mail Process Completed")