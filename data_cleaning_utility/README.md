# 🧹 Data Cleaning Utility

A Python-based data cleaning utility that uses **Pandas** to process CSV datasets and prepare cleaner, more consistent data.

The project detects and handles missing values, removes duplicate records, standardizes column names, and saves the cleaned dataset as a new CSV file.

---

## 🚀 Features

- 📂 Read CSV files
- 🔍 Detect missing values
- 🧩 Fill missing values
- 🗑️ Remove duplicate records
- ✨ Standardize column names
- 💾 Save cleaned data to a new CSV file

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.x | Core programming |
| Pandas | Data processing and cleaning |

---

## 🔄 Data Cleaning Workflow

```text
CSV Dataset
     ↓
Read Dataset
     ↓
Detect Missing Values
     ↓
Fill Missing Values
     ↓
Remove Duplicate Records
     ↓
Standardize Column Names
     ↓
Save Cleaned Dataset

## Project Structure

```
data_cleaning_utility/
│
├── data/
│   └── employees.csv
│
├── output/
│   └── cleaned_data.csv
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

## Output

The cleaned dataset is saved as:

```
output/cleaned_data.csv
```

## Author

**Satyendra Singh**
GitHub: https://github.com/SATY8542
