"""
main.py

Entry point for Assignment 2 – Sales Analysis.
Loads the CSV file and prints a full analytical summary to console.
"""

from __future__ import annotations

from pathlib import Path

from io_utils import load_sales_from_csv
from sales_analysis import SalesAnalyzer


def main() -> None:
    # Path: Assignment2/data/sales.csv
    csv_path = Path(__file__).parent / "data" / "sales.csv"

    # Load sales records into SaleRecord objects
    sales = load_sales_from_csv(csv_path)

    # Create analyzer
    analyzer = SalesAnalyzer(sales)

    summary = analyzer.summary()

    print("===== SALES ANALYTICS =====")
    print(f"Total records: {len(sales)}")

    print("\n--- Overall Metrics ---")
    print(f"Total revenue:         {summary['total_revenue']:.2f}")
    print(f"Average order value:   {summary['average_order_value']:.2f}")
    print(f"Returns rate:          {summary['returns_rate'] * 100:.2f}%")

    print("\n--- Revenue by Country ---")
    for country, revenue in summary["revenue_by_country"].items():
        print(f"{country:15s} {revenue:10.2f}")

    print("\n--- Revenue by Category ---")
    for category, revenue in summary["revenue_by_category"].items():
        print(f"{category:15s} {revenue:10.2f}")

    print("\n--- Monthly Revenue (YYYY-MM) ---")
    for (year, month), revenue in summary["monthly_revenue"].items():
        print(f"{year}-{month:02d}:     {revenue:10.2f}")

    print("\n--- Top Customers by Revenue ---")
    for customer_id, revenue in summary["top_customers_by_revenue"]:
        print(f"{customer_id:10s} {revenue:10.2f}")


if __name__ == "__main__":
    main()
