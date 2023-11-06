# Graph_Hello_World
### In this repository, we will:
- First, run some basic algorithm on graphs
- Second, try to add errors\bugs\faults into graph\code, then apply delta debugging(and other SE techniques) to make everything correct again.
- 3, try to diverse single graph to set of graphs.
- 4, Generate different type of graphs and run basic algorithms on it. 






## 1,Select real dataset and run classic graph algorithms on it

In  `Basic_Algorithm.py ` , I implemented `Dijkstra`, which could find out SSSP between 2 points, and `BFS`, which could count the size of a connected-component as well as the longest path started\ended at a point. 




## 3,Generate different set of graphs from single graph

There are 3 general ideas about how to generate new graphs.

1, Use domain-specific graph-generating pattern. Here my data is academic-relationship in physics field, so  I use 

2, Borrow graph processing ideas from existing papers.

3, Generate specific type of graph, like `part 4`

## 4,Generate different type of graphs and run basic algorithms on it. 

We will try to generate\find different types of graph and then run basic graph algorithms on them.  By doing so, we hope to find future practical research ideas\methods. 

| Graph\Algorithm       | Dijkstra(SSSP) | Todo :Size of Connected component(BFS) | Todo: Max flow(min cut) | ...  |
| --------------------- | -------------- | -------------------------------------- | ----------------------- | ---- |
| Original CA Road map  |                |                                        |                         |      |
| Original Relationship |                |                                        |                         |      |
| Dense                 |                |                                        |                         |      |
|                       |                |                                        |                         |      |
| Tree                  |                |                                        |                         |      |
|                       |                |                                        |                         |      |
| Connected             |                |                                        |                         |      |
|                       |                |                                        |                         |      |
| Forest                |                |                                        |                         |      |
|                       |                |                                        |                         |      |
| Pseudograph           |                |                                        |                         |      |
|                       |                |                                        |                         |      |
|                       |                |                                        |                         |      |
| ...                   |                |                                        |                         |      |













# Index

 Datasets 

| Name                                                         | Domains                                                    |      |      |      |      |      |      |      |      |
| ------------------------------------------------------------ | ---------------------------------------------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| [Stanford Large Network Dataset Collection](https://snap.stanford.edu/data/) | Social network, communities, communications, citations,... |      |      |      |      |      |      |      |      |
|                                                              |                                                            |      |      |      |      |      |      |      |      |
|                                                              |                                                            |      |      |      |      |      |      |      |      |
|                                                              |                                                            |      |      |      |      |      |      |      |      |
|                                                              |                                                            |      |      |      |      |      |      |      |      |
|                                                              |                                                            |      |      |      |      |      |      |      |      |
|                                                              |                                                            |      |      |      |      |      |      |      |      |
|                                                              |                                                            |      |      |      |      |      |      |      |      |
|                                                              |                                                            |      |      |      |      |      |      |      |      |



Basic graph types 

| Types                    | Explanation                                                  | Chosen |      |      |      |
| ------------------------ | ------------------------------------------------------------ | ------ | ---- | ---- | ---- |
| Undirected Graph         | Graph without directions                                     |        |      |      |      |
| Directed Graph           | Graph with directions                                        |        |      |      |      |
| Simple Graph             | A graph with no loops and no multiple edges between vertices. |        |      |      |      |
| Multigraph               | A graph that allows multiple edges but no loops.             |        |      |      |      |
| Pseudograph              | A graph that allows both multiple edges and loops.           |        |      |      |      |
| Connected Graph          | An undirected graph in which there is a path between every pair of vertices. |        |      |      |      |
| Strongly Connected Graph | A directed graph in which there is a directed path between every pair of distinct vertices. |        |      |      |      |
| Complete Graph           | A graph in which there is exactly one edge between every pair of distinct vertices |        |      |      |      |
| Bipartite Graph          | A graph whose vertex set can be partitioned into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other set. |        |      |      |      |
| Weighted Graph           |                                                              |        |      |      |      |
| Tree                     |                                                              |        |      |      |      |
| Forest                   | A graph that is a disjoint union of trees.                   |        |      |      |      |
| Planar Graph             | A graph that can be drawn on the plane without edges crossing. |        |      |      |      |
| Regular Graph            | A graph in which every vertex has the same degree.           |        |      |      |      |
| Self-loop Graph          | a self-loop in a graph occurs when an edge connects a vertex to itself. |        |      |      |      |
| Star Graph               | a single central vertex is connected to all other vertices, and there are no other edges |        |      |      |      |
| Cycle Graph:             | A cycle graph is a graph that forms a single cycle           |        |      |      |      |
| Grid Graph               | A grid graph is a 2-dimensional graph where vertices are arranged in rows and columns, and each vertex is connected to its neighboring vertices (above, below, left, and right, but not diagonally) |        |      |      |      |
| Hypergraph               | A generalization of a graph where an edge can connect more than two vertices |        |      |      |      |
| Spare graph              |                                                              |        |      |      |      |
| dense graph              |                                                              |        |      |      |      |

Basic Graph concepts

| Concepts       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| -------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Dominating set |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
|                |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
|                |      |      |      |      |      |      |      |      |      |      |      |      |      |      |

