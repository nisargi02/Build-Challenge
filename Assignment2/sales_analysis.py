from __future__ import annotations
from collections import defaultdict
from typing import Callable, Dict, Iterable, List, Tuple
from analysis import (
    average_order_value,
    monthly_revenue,
    returns_rate,
    revenue_by_category,
    revenue_by_country,
    top_n_customers_by_revenue,
    total_revenue,
)
from models import SaleRecord

# -------------------------------------------------------------------
# Class-Based API (Wrapper Around Functional Analytics)
# -------------------------------------------------------------------

class SalesAnalyzer:
    """
    Object-oriented wrapper around the functional sales analysis utilities.

    This class:
    - Encapsulates a collection of SaleRecord instances.
    - Exposes high-level analytical methods as instance methods.
    - Delegates actual computation to the pure functions defined above.

    """

    def __init__(self, sales: Iterable[SaleRecord]):
        # Store a local list copy to avoid external mutation issues.
        self._sales: List[SaleRecord] = list(sales)

    # ---------- Core metrics ----------

    def total_revenue(self) -> float:
        """Return total net revenue across all records."""
        return total_revenue(self._sales)

    def average_order_value(self) -> float:
        """Return the average order value across all records."""
        return average_order_value(self._sales)

    def returns_rate(self) -> float:
        """Return the overall returns rate (0–1)."""
        return returns_rate(self._sales)

    # ---------- Grouped aggregations ----------

    def revenue_by_country(self) -> Dict[str, float]:
        """Return net revenue aggregated by country."""
        return revenue_by_country(self._sales)

    def revenue_by_category(self) -> Dict[str, float]:
        """Return net revenue aggregated by category."""
        return revenue_by_category(self._sales)

    def monthly_revenue(self) -> Dict[Tuple[int, int], float]:
        """Return net revenue aggregated by (year, month)."""
        return monthly_revenue(self._sales)

    def top_n_customers_by_revenue(
        self, n: int = 5
    ) -> List[Tuple[str, float]]:
        """Return top N customers by net revenue."""
        return top_n_customers_by_revenue(self._sales, n=n)

    # ---------- Convenience summary ----------

    def summary(self) -> Dict[str, object]:
        """
        Return a dictionary summarizing key analytics.

        Useful for printing a single report from main.py.
        """
        return {
            "total_revenue": self.total_revenue(),
            "average_order_value": self.average_order_value(),
            "returns_rate": self.returns_rate(),
            "revenue_by_country": self.revenue_by_country(),
            "revenue_by_category": self.revenue_by_category(),
            "monthly_revenue": self.monthly_revenue(),
            "top_customers_by_revenue": self.top_n_customers_by_revenue(),
        }
