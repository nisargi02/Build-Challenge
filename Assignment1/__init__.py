"""
Assignment 1: Producer–Consumer pattern with thread synchronization.

This package contains:
- A bounded blocking queue implementation.
- Producer and consumer thread classes.
- A pipeline that wires them together.
"""

from .blocking_queue import BoundedBlockingQueue
from .producer import Producer
from .consumer import Consumer
from .pipeline import run_pipeline

__all__ = ["BoundedBlockingQueue", "Producer", "Consumer", "run_pipeline"]
