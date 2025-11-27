"""
consumer.py

Consumer thread that reads from a shared blocking queue
and stores items in a destination container.
"""

import threading
from typing import Any, List

from blocking_queue import BoundedBlockingQueue
from logging_utils import log

class Consumer(threading.Thread):
    """
    Consumer thread.

    - Reads items from a BoundedBlockingQueue.
    - Stores them into a destination container.
    - Stops when it encounters the sentinel.
    """

    def __init__(
        self,
        queue: BoundedBlockingQueue,
        destination: List[Any],
        sentinel: Any = None,
    ) -> None:
        super().__init__(name="ConsumerThread")
        self._queue = queue
        self._destination = destination
        self._sentinel = sentinel

    def run(self) -> None:
        while True:
            item = self._queue.get()
            if item == self._sentinel:
                # No re-insertion needed since we have only one consumer.
                log("Received sentinel, consumer exiting.")
                break
            self._destination.append(item)
            log(f"Consumed {item} (queue size={self._queue.size()})")
