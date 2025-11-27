"""
run_assignment1.py

Entry point script for Assignment 1.

Demonstrates:
- Thread synchronization
- Concurrent programming
- Blocking queue behavior
- Wait/notify mechanism via Condition
"""

from pipeline import run_pipeline


def main() -> None:
    source_items = [f"item-{i}" for i in range(1, 11)]

    destination_items = run_pipeline(
        source=source_items,
        buffer_capacity=3,
        sentinel=None,  # Using None as sentinel
    )

    print("=== Assignment 1: Producer–Consumer Demo ===")
    print("Source container:     ", source_items)
    print("Destination container:", destination_items)


if __name__ == "__main__":
    main()
