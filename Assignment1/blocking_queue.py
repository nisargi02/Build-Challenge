"""
blocking_queue.py

Bounded blocking queue implemented using threading.Condition,
demonstrating wait/notify-based synchronization.
"""

import threading
from typing import Any, List


class BoundedBlockingQueue:
    """
    A bounded blocking queue.

    Responsibilities:
    - Block producers when the queue is full.
    - Block consumers when the queue is empty.
    - Coordinate threads via wait()/notify() on Condition variables.
    """

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Queue capacity must be positive")

        self._capacity = capacity
        self._buffer: List[Any] = []

        self._lock = threading.Lock()
        self._not_empty = threading.Condition(self._lock)
        self._not_full = threading.Condition(self._lock)

    def put(self, item: Any) -> None:
        """
        Put an item into the queue.
        Blocks if the queue is full until space becomes available.
        """
        with self._not_full:
            while len(self._buffer) >= self._capacity:
                self._not_full.wait()

            self._buffer.append(item)
            # Notify one waiting consumer that an item is available.
            self._not_empty.notify()

    def get(self) -> Any:
        """
        Remove and return an item from the queue.
        Blocks if the queue is empty until an item is available.
        """
        with self._not_empty:
            while not self._buffer:
                self._not_empty.wait()

            item = self._buffer.pop(0)
            # Notify one waiting producer that space is available.
            self._not_full.notify()
            return item

    def size(self) -> int:
        """Return current number of items in the queue (non-blocking)."""
        with self._lock:
            return len(self._buffer)

    @property
    def capacity(self) -> int:
        return self._capacity
