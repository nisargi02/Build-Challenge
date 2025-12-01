# Sales Analysis – Functional Programming with Streams

## Overview
This project demonstrates functional-style data analysis over CSV sales data in Python.  


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
The assignment requires implementing classes. SaleRecord models CSV rows, and SalesAnalyzer provides a clean OO wrapper around the functional analytics.  
All business logic remains in stateless, testable pure functions.

- Functional analytics for clarity and testability:
Core operations use functional programming patterns (map, lambdas, comprehensions) to align with the assignment’s emphasis on streams.

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

## Why This Dataset Was Chosen

The assignment requires selecting or constructing a CSV dataset suitable for demonstrating functional programming, stream-style operations, and data aggregation.
To meet this requirement, a custom dataset was created that contains a realistic mix of sales transactions.

Reasons for this dataset choice:
- Represents typical sales transaction data with fields commonly found in retail and service workflows.
- Includes numeric fields (quantity, unit price, discount) enabling meaningful revenue calculations.
- Contains multiple categorical dimensions (country, category, product, customer), allowing grouping and aggregation operations.
- Includes returned transactions, enabling conditional logic and edge-case handling.
- Uses a clean, simple schema, letting the focus remain on the analysis logic rather than data cleaning.
- Small enough for unit testing, but representative of patterns seen in larger datasets.

## Dataset Design Considerations & Assumptions

- Date format uses ISO YYYY-MM-DD for easy parsing and sorting.
- Discount values are expressed as fractions (0.20 = 20%).
- Returned orders produce zero net revenue, matching standard accounting treatment.
- Field types map directly to the SaleRecord dataclass for clarity and type safety.
- Categories and countries are varied to support grouping and segmentation.  

This dataset is intentionally compact, but the analysis code is designed to work the same way for thousands of rows.


## Directory Structure
```
Assignment2/
├─ data/
│  └─ sales.csv
├─ tests/
│  ├─ __init__.py
│  └─ test_sales_analysis.py
├─ __init__.py
├─ analysis.py
├─ sales_analysis.py
├─ io_utils.py
├─ main.py
├─ models.py
└─ Readme.md

```


## Setup

git clone ```https://github.com/nisargi02/Build-Challenge.git ```   
cd ```<repository>   ```  

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