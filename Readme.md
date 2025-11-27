### Build Challenge – Concurrent Systems & Functional Data Analysis (Python)

This repository contains solutions to two technical build challenges, demonstrating competency in:  

- Concurrent programming
- Synchronization with condition variables
- Custom bounded blocking queues
- Functional programming
- Stream-style data processing
- Modular software design
- Unit testing and verification  

Both assignments are implemented in Python, fully modular, and include test coverage.

## Assignment1 - Producer–Consumer with Bounded Blocking Queue

A concurrent system implementing:  
- Custom thread-safe bounded queue
- Producer and consumer threads
- Proper blocking on full/empty conditions
- Graceful shutdown via sentinel
- Fully tested pipeline and queue behavior

Detailed README: Assignment1/Readme.md
Code location: Assignment1/

## Assignment 2 – Sales Analysis with Functional Programming

A functional-style analytics engine using:  
- A typed dataclass for modeling sales records
- Lambda expressions, map, filter, grouping logic
- Aggregations: revenue by country, category, month, customer
- CSV parsing using Python stdlib
- Tests covering all analytic functions

Detailed README: Assignment2/Readme.md
Code location: Assignment2/

## Setup

git clone <your-repo-url>.git   
cd <repository>   
cd (Assignment1/Assignemnt2)

python -m venv .venv  
source .venv/bin/activate  (MacOs/Linux)   
.venv\Scripts\activate (Windows)  

## Running the Analysis
python -m main

## Running Tests
python -m unittest discover -s Tests