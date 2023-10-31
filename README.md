# Graph_Hello_World
### In this repository, we will:
- First, run some basic algorithm on graphs
- Second, try to add errors\bugs\faults into graph\code, then apply delta debugging(and other SE techniques) to make everything correct again.
- Third, try to diverse single graph to set of graphs.

## Select real dataset and run classic graph algorithms on it

In  `Basic_Algorithm.py ` , I implemented `Dijkstra`, which could find out SSSP between 2 points, and `BFS`, which could count the size of a connected-component as well as the longest path started\ended at a point. 



## Generate different set of graphs from single graph

There are 3 general ideas about how to generate new graphs.

1, Use domain-specific graph-generating pattern. Here my data is academic-relationship in physics field, so  I use 

2, Borrow graph processing ideas from existing papers.

3, Generate specific type of graph, like circled graph\ 

