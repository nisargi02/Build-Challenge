from __future__ import annotations

from collections import defaultdict
from typing import Callable, Dict, Iterable, List, Tuple

from models import SaleRecord


def total_revenue(sales: Iterable[SaleRecord]) -> float:
    """Total net revenue over all (non-returned) sales."""
    # functional style: sum + map + lambda
    return sum(map(lambda s: s.net_amount, sales))


def revenue_by_country(sales: Iterable[SaleRecord]) -> Dict[str, float]:
    """
    Aggregate net revenue per country, sorted by revenue descending.
    """
    totals: Dict[str, float] = defaultdict(float)
    for s in sales:
        totals[s.country] += s.net_amount

    # returning a normal dict but sorted for deterministic output
    return dict(
        sorted(totals.items(), key=lambda kv: kv[1], reverse=True)
    )


def average_order_value(sales: Iterable[SaleRecord]) -> float:
    """
    Average net revenue per order.
    """
    amounts: List[float] = list(map(lambda s: s.net_amount, sales))
    if not amounts:
        return 0.0
    return sum(amounts) / len(amounts)


def top_n_customers_by_revenue(
    sales: Iterable[SaleRecord], n: int = 5
) -> List[Tuple[str, float]]:
    """
    Top N customers by total net revenue.
    Returns list of (customer_id, revenue) sorted descending.
    """
    totals: Dict[str, float] = defaultdict(float)
    for s in sales:
        totals[s.customer_id] += s.net_amount

    sorted_customers = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_customers[:n]


def monthly_revenue(
    sales: Iterable[SaleRecord],
) -> Dict[Tuple[int, int], float]:
    """
    Monthly revenue trend.
    Returns dict keyed by (year, month) with total net revenue.
    Sorted by (year, month) ascending.
    """
    totals: Dict[Tuple[int, int], float] = defaultdict(float)
    for s in sales:
        key = (s.order_date.year, s.order_date.month)
        totals[key] += s.net_amount

    return dict(sorted(totals.items(), key=lambda kv: kv[0]))


def returns_rate(sales: Iterable[SaleRecord]) -> float:
    """
    Percentage of orders marked as returned, in range [0,1].
    """
    sales_list = list(sales)
    if not sales_list:
        return 0.0
    returned_count = sum(map(lambda s: 1 if s.returned else 0, sales_list))
    return returned_count / len(sales_list)


def generic_group_sum(
    sales: Iterable[SaleRecord],
    key_fn: Callable[[SaleRecord], str],
    value_fn: Callable[[SaleRecord], float],
) -> Dict[str, float]:
    """
    Example of a reusable, functional-style grouping helper.
    Groups by key_fn(s) and sums value_fn(s).
    """
    totals: Dict[str, float] = defaultdict(float)
    for s in sales:
        totals[key_fn(s)] += value_fn(s)
    return dict(totals)


def revenue_by_category(sales: Iterable[SaleRecord]) -> Dict[str, float]:
    """
    Revenue per category using the generic_group_sum functional helper.
    """
    return generic_group_sum(
        sales,
        key_fn=lambda s: s.category,
        value_fn=lambda s: s.net_amount,
    )
