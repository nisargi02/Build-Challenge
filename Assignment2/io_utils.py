from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from typing import List

from models import SaleRecord

DATE_FORMAT = "%Y-%m-%d"


def _parse_bool(value: str) -> bool:
    return str(value).strip().upper() in {"TRUE", "T", "1", "YES", "Y"}


def load_sales_from_csv(path: str | Path) -> List[SaleRecord]:
    """
    Load sales data from a CSV file into a list of SaleRecord objects.

    Required headers:
      order_id, order_date, country, category, product, customer_id,
      quantity, unit_price, discount, returned
    """
    path = Path(path)

    # 1) File existence check
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        # 2) CSV schema validation
        required_cols = {
            "order_id", "order_date", "country", "category", "product",
            "customer_id", "quantity", "unit_price", "discount", "returned",
        }

        missing = required_cols - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"CSV missing required columns: {missing}")

        records: List[SaleRecord] = []

        for row in reader:
            # 3) Defensive date parsing
            try:
                order_date = datetime.strptime(row["order_date"], DATE_FORMAT).date()
            except ValueError:
                raise ValueError(f"Invalid date format in row: {row}")

            # 4) Convert and build SaleRecord
            records.append(
                SaleRecord(
                    order_id=row["order_id"],
                    order_date=order_date,
                    country=row["country"],
                    category=row["category"],
                    product=row["product"],
                    customer_id=row["customer_id"],
                    quantity=int(row["quantity"]),
                    unit_price=float(row["unit_price"]),
                    discount=float(row["discount"]),
                    returned=_parse_bool(row["returned"]),
                )
            )

    return records
