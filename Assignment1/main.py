"""
main.py

Demonstrates:
- Thread synchronization
- Concurrent programming
- Blocking queue behavior
- Wait/notify mechanism via Condition
"""

from pipeline import run_pipeline

def main() -> None:
    source_items = [f"item-{i}" for i in range(1, 11)]

    result = run_pipeline(
        source=source_items,
        buffer_capacity=3,
        sentinel=None,  # Using None as sentinel; safe because items are strings
    )

    print("=== Assignment 1: Producer–Consumer Demo ===")
    print("Source container:      ", source_items)
    print("Destination container: ", result.destination)
    print("Produced count:        ", result.produced_count)
    print("Consumed count:        ", result.consumed_count)


if __name__ == "__main__":
    main()

