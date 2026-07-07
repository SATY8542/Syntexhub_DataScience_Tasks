# Pandas CSV Reader & Basic Analysis

## Project Description
This project demonstrates how to use the Pandas library to read CSV files, explore datasets, perform basic data analysis, filter data, and save the processed results. It is designed to help beginners understand essential data manipulation techniques in Python.

## Features
- Read CSV file into a Pandas DataFrame
- Display the first and last records
- Check column names and data types
- Generate summary statistics
- Filter rows based on conditions
- Save filtered data to a new CSV file

## Technologies Used
- Python 3.x
- Pandas
- OpenPyXL (optional, for Excel support)

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