# Sales Analysis – Functional Programming with Streams (Python)

## Overview
This project demonstrates functional-style data analysis over CSV sales data in Python.
It mirrors Java Stream-style operations using Python's functional APIs (map, filter, lambdas) and aggregation patterns.

### Key Objectives

-Functional programming
-Stream-like operations over CSV records
-Data aggregation and grouping
-Lambda expressions and higher-order functions

## Dataset

File: data/sales.csv

### Columns

order_id (string)
order_date (YYYY-MM-DD)
country (string)
category (string)
product (string)
customer_id (string)
quantity (int)
unit_price (float)
discount (float, 0–1)
returned (TRUE / FALSE)

### Assumptions

-discount is a fraction (e.g., 0.15 = 15%).
-Returned orders contribute 0 to net revenue.
-order_date uses ISO format YYYY-MM-DD.

## Directory Structure
Assignment2/
├─ Data/
│  └─ sales.csv
├─ Tests/
│  ├─ __init__.py
│  └─ test_sales_analysis.py
├─ __init__.py
├─ analysis.py
├─ io_utils.py
├─ main.py
├─ models.py
└─ Readme.md



## Setup

git clone <your-repo-url>.git
cd Assignment2

python -m venv .venv
source .venv/bin/activate (Windows: .venv\Scripts\activate)


## Running the Analysis

python -m main

## Sample Output

===== SALES ANALYTICS =====
Total records: 5000

--- Overall Metrics ---
Total revenue: 1234567.89
Average order value: 245.67
Returns rate: 3.40%

--- Revenue by Country ---
USA 789000.00
Canada 250000.00
Germany 195000.00
...

--- Revenue by Category ---
Electronics 500000.00
Accessories 300000.00
...

--- Monthly Revenue (YYYY-MM) ---
2024-01: 80000.00
2024-02: 95000.00
...

--- Top Customers by Revenue ---
C1023 15000.00
C0501 12000.00
...

## Running Tests

python -m unittest discover -s tests