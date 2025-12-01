from __future__ import annotations

import unittest
from datetime import date

from analysis import (
    average_order_value,
    generic_group_sum,
    monthly_revenue,
    returns_rate,
    revenue_by_category,
    revenue_by_country,
    top_n_customers_by_revenue,
    total_revenue,
)
from models import SaleRecord


def _sample_sales():
    # 5 sample rows, including a return and multiple countries/categories
    return [
        SaleRecord(
            order_id="O1",
            order_date=date(2024, 1, 10),
            country="USA",
            category="Electronics",
            product="Laptop",
            customer_id="C1",
            quantity=1,
            unit_price=1000.0,
            discount=0.10,  # 10%
            returned=False,
        ),
        SaleRecord(
            order_id="O2",
            order_date=date(2024, 1, 15),
            country="USA",
            category="Accessories",
            product="Mouse",
            customer_id="C2",
            quantity=2,
            unit_price=25.0,
            discount=0.0,
            returned=False,
        ),
        SaleRecord(
            order_id="O3",
            order_date=date(2024, 2, 5),
            country="Canada",
            category="Electronics",
            product="Monitor",
            customer_id="C1",
            quantity=1,
            unit_price=200.0,
            discount=0.0,
            returned=True,  # should not contribute to revenue
        ),
        SaleRecord(
            order_id="O4",
            order_date=date(2024, 2, 20),
            country="Canada",
            category="Accessories",
            product="Keyboard",
            customer_id="C3",
            quantity=1,
            unit_price=50.0,
            discount=0.0,
            returned=False,
        ),
        SaleRecord(
            order_id="O5",
            order_date=date(2024, 2, 25),
            country="USA",
            category="Electronics",
            product="Headphones",
            customer_id="C1",
            quantity=1,
            unit_price=150.0,
            discount=0.20,  # 20%
            returned=False,
        ),
    ]


class TestAnalysis(unittest.TestCase):
    def setUp(self) -> None:
        self.sales = _sample_sales()

    def test_total_revenue(self):
        # O1: 1000 * 0.9 = 900
        # O2: 2 * 25 = 50
        # O3: returned -> 0
        # O4: 1 * 50 = 50
        # O5: 150 * 0.8 = 120
        expected = 900 + 50 + 0 + 50 + 120
        self.assertAlmostEqual(total_revenue(self.sales), expected, places=2)

    def test_revenue_by_country(self):
        result = revenue_by_country(self.sales)
        # USA: O1 + O2 + O5
        usa_expected = 900 + 50 + 120
        canada_expected = 50  # only O4 (O3 returned)
        self.assertAlmostEqual(result["USA"], usa_expected, places=2)
        self.assertAlmostEqual(result["Canada"], canada_expected, places=2)

    def test_average_order_value(self):
        total = total_revenue(self.sales)
        expected = total / len(self.sales)
        self.assertAlmostEqual(average_order_value(self.sales), expected, places=4)

    def test_top_n_customers_by_revenue(self):
        top2 = top_n_customers_by_revenue(self.sales, n=2)
        # Customer C1: O1 (900) + O3 (0) + O5 (120) = 1020
        # Customer C2: O2 (50)
        # Customer C3: O4 (50)
        self.assertEqual(top2[0][0], "C1")
        self.assertAlmostEqual(top2[0][1], 1020.0, places=2)
        self.assertIn(top2[1][0], ["C2", "C3"])
        self.assertAlmostEqual(top2[1][1], 50.0, places=2)
        self.assertEqual(len(top2), 2)

    def test_monthly_revenue(self):
        result = monthly_revenue(self.sales)
        # Jan: O1 (900) + O2 (50) = 950
        # Feb: O3 (0) + O4 (50) + O5 (120) = 170
        self.assertAlmostEqual(result[(2024, 1)], 950.0, places=2)
        self.assertAlmostEqual(result[(2024, 2)], 170.0, places=2)

    def test_returns_rate(self):
        # 1 returned out of 5
        self.assertAlmostEqual(returns_rate(self.sales), 1.0 / 5.0, places=4)

    def test_generic_group_sum_and_revenue_by_category(self):
        # test generic helper
        result = generic_group_sum(
            self.sales,
            key_fn=lambda s: s.country,
            value_fn=lambda s: s.net_amount,
        )
        self.assertIn("USA", result)
        self.assertIn("Canada", result)

        # test revenue_by_category wrapper
        category_revenue = revenue_by_category(self.sales)
        self.assertIn("Electronics", category_revenue)
        self.assertIn("Accessories", category_revenue)

    def test_top_n_more_than_customers(self):
        sales = _sample_sales()
        top10 = top_n_customers_by_revenue(sales, n=10)
        # Should just return all distinct customers, not crash
        self.assertLessEqual(len(top10), len({s.customer_id for s in sales}))

    def test_top_n_zero(self):
        sales = _sample_sales()
        top0 = top_n_customers_by_revenue(sales, n=0)
        self.assertEqual(top0, [])

    def test_empty_sales_total_and_rates(self):
        empty: list[SaleRecord] = []

        self.assertEqual(total_revenue(empty), 0.0)
        self.assertEqual(revenue_by_country(empty), {})
        self.assertEqual(monthly_revenue(empty), {})

        # Whatever your implementation does here – either 0.0 or raises
        # If you chose 0.0:
        self.assertEqual(average_order_value(empty), 0.0)

        # returns_rate: again depends on your implementation;
        # common choice is 0.0 for "no data".
        self.assertEqual(returns_rate(empty), 0.0)
    
    def test_all_returns(self):
        #to check returns don’t contribute to revenue
        returned_sales = [
            SaleRecord(
                order_id="R1",
                order_date=date(2024, 3, 1),
                country="USA",
                category="Electronics",
                product="Camera",
                customer_id="C9",
                quantity=1,
                unit_price=500.0,
                discount=0.0,
                returned=True,
            )
        ]

        self.assertEqual(total_revenue(returned_sales), 0.0)
        self.assertEqual(revenue_by_country(returned_sales).get("USA", 0.0), 0.0)
        self.assertAlmostEqual(returns_rate(returned_sales), 1.0, places=4)

    def test_generic_group_sum_empty(self):
         #An empty input should produce an empty dictionary (no groups)
        result = generic_group_sum([], key_fn=lambda s: s.country, value_fn=lambda s: s.net_amount)
        self.assertEqual(result, {})

    def test_revenue_by_country_sums_to_total(self):
        #Sum of country-level revenue should equal total revenue.
        total = total_revenue(self.sales)
        by_country = revenue_by_country(self.sales)
        self.assertAlmostEqual(sum(by_country.values()), total, places=2)

    def test_revenue_by_category_sums_to_total(self):
        #Sum of category-level revenue should equal total revenue.
        total = total_revenue(self.sales)
        by_category = revenue_by_category(self.sales)
        self.assertAlmostEqual(sum(by_category.values()), total, places=2)


class TestSalesAnalyzerWrapper(unittest.TestCase):
    def test_summary(self):
        from sales_analysis import SalesAnalyzer
        analyzer = SalesAnalyzer(_sample_sales())
        summary = analyzer.summary()

        # Structure checks
        self.assertIn("total_revenue", summary)
        self.assertIn("revenue_by_country", summary)
        self.assertIn("top_customers_by_revenue", summary)

        # Sanity check that wrapper delegates correctly
        self.assertAlmostEqual(
            summary["total_revenue"],
            total_revenue(_sample_sales()),
            places=2,
        )
        
if __name__ == "__main__":
    unittest.main()



