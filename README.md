# simplify_360_assignment
This repository is the assignment work given by simplify_360 as a part of their selection process. Questions can be found in the coding assignemtn question.txt file

##Q1:
This console application implements a task scheduler for a complex workflow with task dependencies. The scheduler calculates the earliest and latest completion times for a set of tasks with dependencies, using the Critical Path Method (CPM).

##Overview:
The task scheduler is designed to help manage tasks that have dependencies on other tasks to complete. It calculates:

- **Earliest Completion Time**: The earliest time at which all tasks can be completed.
- **Latest Completion Time**: The latest time by which all tasks can still be completed without delaying the entire project.

## Implementation Details

The scheduler is implemented in Python and uses a directed acyclic graph (DAG) to represent tasks and their dependencies. It uses topological sorting to determine the order of task execution and calculates the earliest and latest start and finish times for each task.

##Q2:
This console application can be used to manage and analyze a friendship network. It can find all the friends of two people, determine common friends, and calculate the "nth connection" (degree of separation) between two people in the network.

##Overview:
The friendship network is represented as an undirected graph where each person is a node, and each friendship is an edge connecting two nodes. The operations are implemented using breadth-first search (BFS) for finding connections.
