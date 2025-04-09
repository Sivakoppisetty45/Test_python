import pandas as pd
import datetime

# Create dummy data
data = {
    "Name": ["Siva", "Lakshmi", "Achyuth"],
    "Role": ["Cloud Engineer", "DevOps Engineer", "Monitoring Lead"],
    "Date": [datetime.date.today()] * 3
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save it to an Excel file
output_file = "team_report.xlsx"
df.to_excel(output_file, index=False)

print(f"[✓] Excel report created: {output_file}")
