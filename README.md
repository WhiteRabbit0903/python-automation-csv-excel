# Python Automation – CSV & Excel Data Processing Tool

## Overview

This project is a Python-based automation tool designed to process CSV and Excel files automatically.

It helps businesses:

- Clean raw data
- Remove duplicates
- Standardize formats
- Transform columns
- Export structured output files
- Reduce manual work

The goal is to automate repetitive data tasks and improve efficiency.

---

## Technologies Used

- Python
- pandas
- NumPy
- Excel / CSV file handling

---

## Example Workflow

1. Load CSV or Excel file
2. Clean missing values
3. Remove duplicates
4. Transform selected columns
5. Export processed file

---

## Example Code

```python
import pandas as pd

def process_file(input_path, output_path):
    df = pd.read_csv(input_path)

    df = df.drop_duplicates()
    df = df.fillna("")

    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    process_file("input.csv", "output.csv")
Autor
Siarhei A.

Следующий шаг:  
мы добавим реальный automation script файл `.py` чтобы проект выглядел как настоящий production инструмент 🚀
