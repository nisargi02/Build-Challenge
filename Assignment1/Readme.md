# Assignment 1 – Producer–Consumer with Bounded Blocking Queue

## Overview
This program simulates concurrent data transfer between:  
A Producer that reads items from a source container  
A Consumer that processes items into a destination container  
A Shared Bounded Queue that enforces blocking behavior when full or empty  


Thread synchronization is implemented using:  
-threading.Lock  
-threading.Condition  
-wait() / notify()  


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
assignment1/
├─ blocking_queue.py         # Custom bounded blocking queue using Condition
├─ producer.py               # Producer thread implementation
├─ consumer.py               # Consumer thread implementation
├─ pipeline.py               # Orchestrates producer + consumer + queue
├─ run_assignment1.py        # Demo executable
└─ tests/
   ├─ test_blocking_queue.py  # Tests blocking behavior + concurrency
   └─ test_pipeline.py        # Tests full pipeline
```

## How to Run the Demo

git clone <your-repo-url>.git  
cd Assignment1

### Create virtual environment
python3 -m venv venv  
source venv/bin/activate (MacOs/Linux)  
venv\Scripts\activate (Windows)  

### Run the demo
python -m main

### Run all tests
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