from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class SaleRecord:
    """
    Represents a single row from the sales CSV.

    Assumed CSV columns:
    - order_id: str
    - order_date: YYYY-MM-DD
    - country: str
    - category: str
    - product: str
    - customer_id: str
    - quantity: int
    - unit_price: float
    - discount: float (0.0–1.0, e.g. 0.10 for 10%)
    - returned: 'TRUE'/'FALSE'
    """
    order_id: str
    order_date: date
    country: str
    category: str
    product: str
    customer_id: str
    quantity: int
    unit_price: float
    discount: float
    returned: bool

    @property
    def gross_amount(self) -> float:
        return self.quantity * self.unit_price

    @property
    def net_amount(self) -> float:
        """Revenue after discount, only if not returned."""
        if self.returned:
            return 0.0
        return self.gross_amount * (1.0 - self.discount)
