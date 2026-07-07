import pandas as pd

# Read CSV file
df = pd.read_csv("data/employees.csv")

print("===== ORIGINAL DATA =====")
print(df)

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Fill missing Age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Salary with average salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Fill missing Department with 'Unknown'
df["Department"] = df["Department"].fillna("Unknown")

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.lower()

# Save cleaned data
df.to_csv("output/cleaned_data.csv", index=False)

print("\n===== CLEANED DATA =====")
print(df)

print("\nData cleaning completed successfully.")
print("Cleaned file saved in output/cleaned_data.csv")