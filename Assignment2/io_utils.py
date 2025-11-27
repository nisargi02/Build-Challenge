from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from typing import Iterable, List

from models import SaleRecord


DATE_FORMAT = "%Y-%m-%d"


def _parse_bool(value: str) -> bool:
    return str(value).strip().upper() in {"TRUE", "T", "1", "YES", "Y"}


def load_sales_from_csv(path: str | Path) -> List[SaleRecord]:
    """
    Load sales data from a CSV file into a list of SaleRecord objects.

    Required headers in CSV:
      order_id,order_date,country,category,product,customer_id,
      quantity,unit_price,discount,returned
    """
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        records: List[SaleRecord] = [
            SaleRecord(
                order_id=row["order_id"],
                order_date=datetime.strptime(row["order_date"], DATE_FORMAT).date(),
                country=row["country"],
                category=row["category"],
                product=row["product"],
                customer_id=row["customer_id"],
                quantity=int(row["quantity"]),
                unit_price=float(row["unit_price"]),
                discount=float(row["discount"]),
                returned=_parse_bool(row["returned"]),
            )
            for row in reader
        ]
    return records
