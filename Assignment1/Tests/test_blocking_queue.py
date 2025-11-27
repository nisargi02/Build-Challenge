"""
Unit tests for BoundedBlockingQueue.

These tests validate:
- Basic queue operations (put/get)
- Correct handling of invalid capacity
- Producer blocking behavior when the queue is full
- Consumer blocking behavior when the queue is empty
- Deadlock detection for robustness

The goal is to ensure correct wait/notify synchronization
and proper behavior under concurrent access.
"""

import unittest
import threading
import time

from blocking_queue import BoundedBlockingQueue


class TestBoundedBlockingQueueBasic(unittest.TestCase):
    """
    Tests for basic, non-concurrent behavior.
    """

    def test_put_and_get_single_item(self):
        """
        Simple functional test:
        - Putting then getting one item should return the same item.
        - Ensures queue works in a single-threaded context.
        """
        q = BoundedBlockingQueue(capacity=1)
        q.put(42)
        self.assertEqual(q.get(), 42)

    def test_capacity_must_be_positive(self):
        """
        The queue must reject invalid capacities.
        - Negative or zero capacities don't make sense.
        - Queue should raise ValueError.
        """
        with self.assertRaises(ValueError):
            BoundedBlockingQueue(0)


class TestBoundedBlockingQueueConcurrency(unittest.TestCase):
    """
    Tests for multi-threaded behavior, blocking, and synchronization.
    """

    def test_producer_blocks_when_queue_full_until_consumer_gets(self):
        """
        Concurrency scenario:

        Setup:
        - Queue capacity = 1
        - Producer will try to put two items
        - First put should succeed immediately
        - Second put should block until the consumer removes the first item

        This test verifies:
        - Correct use of wait()/notify()
        - Producer truly blocks when the queue is full
        - Producer resumes after consumer performs a get()
        """
        q = BoundedBlockingQueue(capacity=1)

        # Fill queue to capacity → next put must block
        q.put("first")

        produced = []
        started_second_put = threading.Event()
        finished_second_put = threading.Event()

        def producer_task():
            # Signal that producer is attempting second put (which should block)
            started_second_put.set()

            q.put("second")     # <- Expected to block here until consumer retrieves "first"
            produced.append("second")

            # Signal successful completion of second put
            finished_second_put.set()

        # Launch producer thread
        t = threading.Thread(target=producer_task, name="ProducerTestThread")
        t.start()

        # Ensure the producer actually reached the blocking put()
        started_second_put.wait(timeout=1.0)

        # Queue must still contain exactly 1 item
        self.assertEqual(q.size(), 1, "Producer did not block as expected")

        # Consumer side: remove the first item → should unblock producer
        self.assertEqual(q.get(), "first")

        # Now producer should finish its second put
        finished_second_put.wait(timeout=1.0)
        self.assertIn("second", produced, "Producer never produced the second item")

        # Ensure the newly added item is returned properly
        self.assertEqual(q.get(), "second")

        # Deadlock guard: producer MUST finish execution
        t.join(timeout=1.0)
        self.assertFalse(t.is_alive(), "Producer thread did not finish (possible deadlock)")

    def test_consumer_blocks_when_queue_empty_until_producer_puts(self):
        """
        Concurrency scenario:

        Setup:
        - Empty queue
        - Consumer immediately tries to get() → expected to block
        - Producer later puts an item, unblocking the consumer

        This test verifies:
        - Correct waiting behavior when queue is empty
        - Consumer resumes correctly once an item is produced
        - No deadlocks occur
        """
        q = BoundedBlockingQueue(capacity=1)

        consumed = []
        consumer_started = threading.Event()
        consumer_finished = threading.Event()

        def consumer_task():
            consumer_started.set()  # Notify test that consumer began executing

            item = q.get()          # <- Expected to block here until something is put
            consumed.append(item)

            consumer_finished.set()  # Notify test that consumer successfully consumed

        # Start consumer thread
        t = threading.Thread(target=consumer_task, name="ConsumerTestThread")
        t.start()

        # Wait for consumer to start and reach the blocking get()
        consumer_started.wait(timeout=1.0)
        time.sleep(0.1)  # Small delay to ensure consumer is blocked

        # No item consumed yet
        self.assertEqual(consumed, [], "Consumer should be blocked but consumed something")

        # Producer puts an item → should unblock consumer
        q.put("value-from-producer")

        # Verify the consumer actually consumed it
        consumer_finished.wait(timeout=1.0)
        self.assertEqual(consumed, ["value-from-producer"])

        # Deadlock guard: consumer MUST finish
        t.join(timeout=1.0)
        self.assertFalse(t.is_alive(), "Consumer thread did not finish (possible deadlock)")


if __name__ == "__main__":
    unittest.main()
