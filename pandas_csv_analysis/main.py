import pandas as pd

# Read CSV file
df = pd.read_csv("data/students.csv")

print("===== DATASET =====")
print(df)

# Head
print("\n===== FIRST 5 ROWS =====")
print(df.head())

# Tail
print("\n===== LAST 5 ROWS =====")
print(df.tail())

# Data Types
print("\n===== DATA TYPES =====")
print(df.dtypes)

# Dataset Information
print("\n===== DATA INFO =====")
print(df.info())

# Summary Statistics
print("\n===== SUMMARY =====")
print(df.describe())

# Mean
print("\nAverage Marks:", df["Marks"].mean())

# Maximum Marks
print("Highest Marks:", df["Marks"].max())

# Minimum Marks
print("Lowest Marks:", df["Marks"].min())

# Count
print("Total Students:", df["Name"].count())

# Filter students having marks greater than 85
filtered = df[df["Marks"] > 85]

print("\n===== FILTERED STUDENTS =====")
print(filtered)

# Select specific columns
selected = df[["Name", "Marks"]]

print("\n===== NAME & MARKS =====")
print(selected)

# Save filtered data
filtered.to_csv("output/filtered_students.csv", index=False)

print("\nFiltered data saved successfully in output folder.")