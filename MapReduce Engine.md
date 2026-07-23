MapReduce Engine

Author: Sankaranarayanan M

Project Overview

This project implements a simple MapReduce Engine in Python to demonstrate how large datasets can be processed efficiently using the MapReduce programming model. The engine simulates the workflow used in distributed computing systems by splitting data into chunks, processing them with mappers, partitioning intermediate results, sorting data, and reducing them to produce the final output.

The project uses a sample dataset containing vegetable names to demonstrate the complete MapReduce pipeline.

Project Structure

```
MapReduce/
│
├── master.py
├── splitter.py
├── mapper.py
├── partitioner.py
├── sorter.py
├── reducer.py
├── input.txt
│
├── chunks/
├── partitions/
└── output/
```

Workflow

1. The input file is divided into smaller chunks.
2. Each chunk is processed independently by a mapper.
3. The mapper generates intermediate key-value pairs in the format `(Vegetable, 1)`.
4. The partitioner distributes the intermediate data among reducers using a hash function.
5. Each partition is sorted so that identical keys are grouped together.
6. The reducer counts the occurrences of each vegetable.
7. The final result is written to `output/result.txt`.

Files Description

* `master.py` – Controls the complete MapReduce workflow.
* `splitter.py` – Splits the input data into multiple chunks.
* `mapper.py` – Converts each input record into a key-value pair.
* `partitioner.py` – Assigns intermediate data to reducer partitions.
* `sorter.py` – Sorts partition files before reduction.
* `reducer.py` – Aggregates values for each key and generates the final output.
* `input.txt` – Sample input dataset.
* `chunks/` – Stores split input files.
* `partitions/` – Stores partitioned and sorted intermediate files.
* `output/` – Stores the final result.

Sample Input

```
Tomato
Potato
Onion
Tomato
Carrot
...
```

Sample Output

```
Beans 2
Brinjal 2
Cabbage 1
Carrot 3
Onion 3
Potato 4
Tomato 5
```

Requirements

* Python 3.x
* No external libraries are required.

How to Run

1. Place the vegetable dataset in `input.txt`.
2. Open a terminal in the project directory.
3. Execute:

```
python master.py
```

The program automatically performs splitting, mapping, partitioning, sorting, and reducing. The final output is generated in the `output` folder as `result.txt`.

Learning Outcomes

* Understand the MapReduce programming model.
* Learn the stages of distributed data processing.
* Implement key-value pair generation.
* Perform hash-based partitioning.
* Group and reduce intermediate data.
* Simulate parallel processing using Python.

License

This project is developed for educational purposes to demonstrate the working principles of the MapReduce Engine.
