# Assignment 1 – Producer–Consumer with Bounded Blocking Queue

## Overview
This program simulates concurrent data transfer between:  
A Producer that reads items from a source container  
A Consumer that processes items into a destination container  
A Shared Bounded Queue that enforces blocking behavior when full or empty  


Thread synchronization is implemented using:  
- threading.Lock  
- threading.Condition  
- wait() / notify()  

## Features Implemented

- Custom bounded blocking queue using Condition variables
- Proper blocking behavior on full/empty buffer
- Dedicated producer and consumer thread classes
- Graceful shutdown using a sentinel value
- End-to-end processing pipeline orchestrator
- Thread-safe shared buffer interactions
- Unit tests covering queue behavior and full pipeline flow
- Console-based logging of producer/consumer actions

## Design Decisions

- Custom blocking queue:  
Implemented a lightweight queue with precise control over wait()/notify() behavior instead of relying on built-in queue.Queue, to demonstrate understanding of condition variables.

- Modular threading components:  
Producer, Consumer, and Pipeline are implemented as separate modules for clarity, reusability, and easier testing.

- Sentinel-based shutdown:  
A sentinel object cleanly signals termination without requiring forced thread interruption.  

- Sentinel choice:  
By default, the pipeline uses `None` as the sentinel value. This is safe for the demo since the data items are non-None strings (e.g., "item-1", "item-2", ...).  
If your data may legitimately contain `None`, you should pass a custom `sentinel` value to `run_pipeline(...)` so that `None` is treated as normal data and only the custom sentinel marks the end of the stream.

- Deterministic logging:  
Timestamps and structured log messages make the execution trace easy to follow and debug.

- Testability:  
Blocking queue logic is tested independently from the pipeline, ensuring correctness of concurrency semantics.

## Architecture
```
+----------------+          +------------------------+          +----------------------+
| Source List    |  --->    | BoundedBlockingQueue   |  --->    | Destination List     |
+----------------+          |  (shared buffer)       |          +----------------------+
                            +------------------------+
                                     /   \
                                    /     \
                             Producer     Consumer
                              Thread       Thread
```

## Flow

1. Producer reads from the source list
2. Producer places items into the bounded queue (put())
3. Consumer takes items from the queue (get())
4. Consumer stores items in the destination list
5. A sentinel value signals completion

## Directory Structure
```
Assignment1/
├─ blocking_queue.py         # Custom bounded blocking queue using Condition
├─ producer.py               # Producer thread implementation
├─ consumer.py               # Consumer thread implementation
├─ pipeline.py               # Orchestrates producer + consumer + queue
├─ main.py        # Demo executable
└─ tests/
   ├─ test_blocking_queue.py  # Tests blocking behavior + concurrency
   └─ test_pipeline.py        # Tests full pipeline
```

## Setup

git clone ```https://github.com/nisargi02/Build-Challenge.git ```   
cd ```<repository>   ```  

python -m venv .venv  
source .venv/bin/activate  (MacOs/Linux)    
.venv\Scripts\activate (Windows)  

cd Assignment1  

## Running the Analysis
python -m main

## Running Tests
python -m unittest discover -s tests

## Sample Output
```
[ProducerThread] 21:43:59 - Produced item-1 (queue size=1)
[ProducerThread] 21:43:59 - Produced item-2 (queue size=2)
[ConsumerThread] 21:43:59 - Consumed item-1 (queue size=1)
[ProducerThread] 21:43:59 - Produced item-3 (queue size=2)
[ConsumerThread] 21:43:59 - Consumed item-2 (queue size=1)
[ProducerThread] 21:43:59 - Produced item-4 (queue size=2)
[ConsumerThread] 21:43:59 - Consumed item-3 (queue size=1)
[ProducerThread] 21:43:59 - Produced item-5 (queue size=2)
[ConsumerThread] 21:43:59 - Consumed item-4 (queue size=1)
[ProducerThread] 21:43:59 - Produced item-6 (queue size=2)
[ConsumerThread] 21:43:59 - Consumed item-5 (queue size=1)
[ProducerThread] 21:43:59 - Produced item-7 (queue size=2)
[ConsumerThread] 21:43:59 - Consumed item-6 (queue size=1)
[ProducerThread] 21:43:59 - Produced item-8 (queue size=2)
[ConsumerThread] 21:43:59 - Consumed item-7 (queue size=1)
[ProducerThread] 21:43:59 - Produced item-9 (queue size=2)
[ConsumerThread] 21:43:59 - Consumed item-8 (queue size=1)
[ProducerThread] 21:43:59 - Produced item-10 (queue size=2)
[ConsumerThread] 21:43:59 - Consumed item-9 (queue size=1)
[ProducerThread] 21:43:59 - Produced sentinel, producer exiting.
[ConsumerThread] 21:43:59 - Consumed item-10 (queue size=1)
[ConsumerThread] 21:43:59 - Received sentinel, consumer exiting.

Source container:      ['item-1', 'item-2', 'item-3', 'item-4', 'item-5', 'item-6', 'item-7', 'item-8', 'item-9', 'item-10']    
Destination container: PipelineResult(destination=['item-1', 'item-2', 'item-3', 'item-4', 'item-5', 'item-6', 'item-7', 'item-8', 'item-9', 'item-10'], produced_count=10, consumed_count=10)
```