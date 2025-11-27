# Sales Analysis – Functional Programming with Streams

## Overview
This project demonstrates functional-style data analysis over CSV sales data in Python.  
It mirrors Java Stream-style operations using Python's functional APIs (map, filter, lambdas) and aggregation patterns.  

## Key Objectives

- Functional programming  
- Stream-like operations over CSV records  
- Data aggregation and grouping  
- Lambda expressions and higher-order functions  

## Features Implemented

- Typed SaleRecord dataclass modeling each CSV row  
- CSV loader with validation and type conversion  
- Stream-style analytical operations: map, filter, grouping, sorting  
- Functional programming patterns with minimal mutation  
- Aggregation: revenue by country, category, customer, and month  
- Computation metrics: total revenue, returns rate, average order value  
- Modular structure with separation of concerns  
- Unit tests covering all analytical functions  
- Console-based report summarizing all analysis 

...


## Design Decisions

- Minimal and meaningful class usage:  
The assignment requires implementing the appropriate classes, which is fulfilled by the SaleRecord dataclass used to model each CSV row. Additional classes were intentionally avoided because they would add unnecessary abstraction without improving clarity.

- Functional analytics for clarity and testability:  
All analysis logic is implemented as pure, stateless functions to align with the assignment’s emphasis on functional programming and stream-style operations. This approach is also more Pythonic, easier to test, and avoids forcing Java-style class structures where they are not needed.

- Modular structure:  
Data modeling, CSV parsing, analytics, and execution are separated into focused modules to keep the codebase clean, maintainable, and easy to extend.  

- Use of built-in CSV and pathlib:  
Avoided external dependencies like Pandas to keep the project lightweight and aligned with the challenge requirements.

- Deterministic sorting:  
Aggregation outputs are sorted for predictable and testable results.

## Extensibility
The current architecture allows easy extension, such as:  
- Adding new metrics (e.g., median order value, customer lifetime value)  
- Supporting alternative file formats (JSON, Parquet)
- Replacing CSV loader with a database source
- Adding CLI flags for selecting analysis modules
- Exporting reports to JSON or HTML

## Dataset
File: data/sales.csv

## Columns
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

## Assumptions

discount is a fraction (e.g., 0.15 = 15%).    
Returned orders contribute 0 to net revenue.  
order_date uses ISO format YYYY-MM-DD.  

## Directory Structure
```
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
```


## Setup

git clone https://github.com/nisargi02/Build-Challenge.git   
cd < repository >  

python -m venv .venv
source .venv/bin/activate  (MacOs/Linux)  
.venv\Scripts\activate (Windows)  

cd Assignment2  

## Running the Analysis
python -m main

## Running Tests
python -m unittest discover -s tests

## Sample Output
```
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

```