from __future__ import annotations

from pathlib import Path

from analysis import (
    average_order_value,
    monthly_revenue,
    returns_rate,
    revenue_by_category,
    revenue_by_country,
    top_n_customers_by_revenue,
    total_revenue,
)
from io_utils import load_sales_from_csv


def main() -> None:
    # Adjust path if needed
    csv_path = Path(__file__).parent.parent/"Assignment2" / "data" / "sales.csv"
    sales = load_sales_from_csv(csv_path)

    print("===== SALES ANALYTICS =====")
    print(f"Total records: {len(sales)}")

    print("\n--- Overall Metrics ---")
    print(f"Total revenue: {total_revenue(sales):.2f}")
    print(f"Average order value: {average_order_value(sales):.2f}")
    print(f"Returns rate: {returns_rate(sales) * 100:.2f}%")

    print("\n--- Revenue by Country ---")
    for country, revenue in revenue_by_country(sales).items():
        print(f"{country:15s} {revenue:10.2f}")

    print("\n--- Revenue by Category ---")
    for category, revenue in revenue_by_category(sales).items():
        print(f"{category:15s} {revenue:10.2f}")

    print("\n--- Monthly Revenue (YYYY-MM) ---")
    for (year, month), revenue in monthly_revenue(sales).items():
        print(f"{year}-{month:02d}: {revenue:10.2f}")

    print("\n--- Top 5 Customers by Revenue ---")
    for customer_id, revenue in top_n_customers_by_revenue(sales, n=5):
        print(f"{customer_id:10s} {revenue:10.2f}")


if __name__ == "__main__":
    main()
