"""
producer.py

Producer thread that reads from a source container
and places items into a shared blocking queue.
"""

import threading
from typing import Iterable, Any

from blocking_queue import BoundedBlockingQueue
from logging_utils import log

class Producer(threading.Thread):
    """
    Producer thread.

    - Reads items from a source container (iterable).
    - Puts each item into the shared BoundedBlockingQueue.
    - After producing all items, sends a sentinel to signal completion.
    """

    def __init__(
        self,
        source: Iterable[Any],
        queue: BoundedBlockingQueue,
        sentinel: Any = None,
    ) -> None:
        super().__init__(name="ProducerThread")
        self._source = list(source)
        self._queue = queue
        self._sentinel = sentinel

    def run(self) -> None:
        for item in self._source:
            self._queue.put(item)

            #have added logging just to check concurrency
            log(f"Produced {item} (queue size={self._queue.size()})")
        # Signal end-of-stream with sentinel.
        self._queue.put(self._sentinel)
        log("Produced sentinel, producer exiting.")
