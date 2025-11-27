import unittest
from pipeline import run_pipeline


class TestProducerConsumerPipeline(unittest.TestCase):
    """
    Tests the end-to-end producer–consumer pipeline using a bounded blocking queue.
    Each test validates a different concurrency or data-transfer scenario.
    """

    def test_all_items_transferred_in_order(self):
        """
        Basic correctness:
        - Ensures all items produced appear in the destination.
        - Ensures ordering (FIFO) is preserved through the queue.
        - Ensures producer and consumer counts match.
        """
        source = [1, 2, 3, 4, 5]
        result = run_pipeline(
            source=source,
            buffer_capacity=2,
            sentinel=None,
        )

        self.assertEqual(result.destination, source)
        self.assertEqual(result.produced_count, result.consumed_count)

    def test_empty_source(self):
        """
        Edge Case:
        - Source container is empty.
        - Pipeline should handle gracefully.
        - No data should be produced or consumed.
        """
        source = []
        result = run_pipeline(
            source=source,
            buffer_capacity=3,
            sentinel=None,
        )

        self.assertEqual(result.destination, [])
        self.assertEqual(result.produced_count, 0)
        self.assertEqual(result.consumed_count, 0)

    def test_small_buffer_capacity_handles_larger_input(self):
        """
        Concurrency Stress Test:
        - Queue capacity = 1 (forces max contention).
        - Source has many items.
        - Ensures no deadlock occurs even when producer/consumer alternate blocking.
        - Order must still be preserved.
        """
        source = list(range(50))
        result = run_pipeline(
            source=source,
            buffer_capacity=1,  # Minimal capacity stresses wait/notify behavior
            sentinel=None,
        )

        self.assertEqual(result.destination, source)
        self.assertEqual(result.produced_count, result.consumed_count)

    def test_custom_sentinel_allows_none_in_data(self):
        """
        Sentinel Handling:
        - Verifies pipeline works when source contains None (valid data).
        - Ensures custom sentinel is correctly recognized as 'end of stream'.
        - None values must still appear in destination exactly as produced.
        """
        source = [1, None, 2, None, 3]
        sentinel = "END"

        result = run_pipeline(
            source=source,
            buffer_capacity=3,
            sentinel=sentinel,
        )

        self.assertEqual(result.destination, source)
        self.assertEqual(result.produced_count, result.consumed_count)


if __name__ == "__main__":
    unittest.main()
