# 📊 Pandas CSV Reader & Basic Analysis

A beginner-friendly Python project that demonstrates how to use **Pandas** to read CSV files, explore datasets, perform basic data analysis, filter data, and save processed results.

---

## 🚀 Features

- 📂 Read CSV files into a Pandas DataFrame
- 👀 Display the first and last records
- 🏷️ Check column names and data types
- 📊 Generate summary statistics
- 🔎 Filter rows based on conditions
- 💾 Save filtered data to a new CSV file

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.x | Core programming |
| Pandas | Data manipulation and analysis |
| OpenPyXL | Optional Excel support |

---

## 🔄 Data Analysis Workflow

```text
CSV Dataset
     ↓
Read CSV using Pandas
     ↓
Explore Dataset
     ↓
Check Columns & Data Types
     ↓
Generate Summary Statistics
     ↓
Filter Data
     ↓
Save Processed Data
     ↓
output/filtered.csv

## Project Structure

```
pandas_csv_analysis/
│
├── data/
│   └── students.csv
│
├── output/
│   └── filtered.csv
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project folder:
   ```bash
   cd pandas_csv_analysis
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Run the Project

```bash
python main.py
```

## Input

The project reads data from:

```
data/students.csv
```

## Output

The program:
- Displays the dataset
- Shows summary statistics
- Filters students based on the specified condition
- Saves the filtered data as:

```
output/filtered.csv
```

## Sample Dataset

| Name | Age | Marks |
|------|-----|-------|
| Rahul | 20 | 85 |
| Aman | 22 | 91 |
| Priya | 21 | 78 |
| Neha | 20 | 88 |

## Future Improvements
- Data visualization using Matplotlib
- Interactive user input
- Support for multiple CSV files
- Advanced filtering options

## Author

**Satyendra Singh**
GitHub: https://github.com/SATY8542