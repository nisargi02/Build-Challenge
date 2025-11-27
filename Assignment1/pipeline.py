"""
pipeline.py

Orchestrates the classic producer-consumer pipeline:

- A source container (input).
- A shared bounded blocking queue (communication channel).
- One producer thread.
- One consumer thread.
- A destination container (output).
"""

from typing import Iterable, Any, List

from blocking_queue import BoundedBlockingQueue
from producer import Producer
from consumer import Consumer
from dataclasses import dataclass

@dataclass
class PipelineResult:
    destination: list
    produced_count: int
    consumed_count: int

def run_pipeline(
    source: Iterable[Any],
    buffer_capacity: int = 5,
    sentinel: Any = None,
) -> PipelineResult:
    """
    Run a single-producer, single-consumer pipeline.

    :param source: Items to be produced (source container).
    :param buffer_capacity: Capacity of the shared blocking queue.
    :param sentinel: Sentinel value used to signal end-of-stream.
    :return: Destination container with all items consumed from the queue.
    """
    queue = BoundedBlockingQueue(capacity=buffer_capacity)
    produced_count = len(list(source))
    destination: List[Any] = []

    producer = Producer(source=source, queue=queue, sentinel=sentinel)
    consumer = Consumer(queue=queue, destination=destination, sentinel=sentinel)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    return PipelineResult(
        destination=destination,
        produced_count=produced_count,
        consumed_count=len(destination),
    )
