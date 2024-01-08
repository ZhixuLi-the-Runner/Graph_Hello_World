# Graph_Hello_World
## Function for each file

| Name               | Description                                 |
| ------------------ | ------------------------------------------- |
| Basic_algorithm.py | Classic graph algorithm for raw input graph |
| main.py            | main function that call other function      |
|                    |                                             |
|                    |                                             |
|                    |                                             |
|                    |                                             |



### Experiment 1: AFL for graph input

We will run  testing tools like AFL、JQF for graph input with different characteristics and see what could remain after running such testing tools.

### AFL test

#### AFL install and hello world

Run a AFL hello world program

First , install AFL

```bash
sudo apt update
sudo apt install afl
```

then write a hello program

```bash
cd ~;mkdir AFL_helloworld
vim hello.c
```

then input  a simple test case

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}

```

Then compile this program with AFL's compiler, which could **insert necessary testing code**

```
 afl-gcc -o hello hello.c
```

then we are ready to run AFL fuzzing test

```bash
mkdir input; echo "example" > input/example.txt;mkdir output
```

here the input and output are folders that store **initial input**  and **testing result**.

```bash
afl-fuzz -i input -o output -- ./hello
```

#### When to finish

AFL doesn't have a predefined end point, needing manually stop(until system resources are exhausted)

Here are the common scenarios when you might choose to stop it:

1. **Sufficient Coverage Achieved**: If AFL has been running for a significant amount of time and the code coverage or the discovery of new paths has **plateaued**, it might be a good time to stop.
2. **Resources Limitation**: If the system starts to struggle due to resource limitations like CPU, memory, or disk space, it might be necessary to stop the fuzzing process.
3. **Finding Bugs**: If AFL has found critical bugs that need to be addressed, you might stop the process, fix the bugs, and then restart fuzzing.
4. **Time Constraints**: In some cases, you might have a specific time frame for fuzzing. Once this time is up, you would stop the process.

You can `Ctrl + C` to end AFL.

#### AFL result analysis

The `output `  folder have multiple subfolders and files, including

| Name         | store                                           |
| ------------ | ----------------------------------------------- |
| queue/       | All input that cause specific crashes and hangs |
| crashes/     | input that cause crashes                        |
| hangs/       | input that cause hang\overtime                  |
| fuzzer_stats |                                                 |
| plot_data    |                                                 |
| fuzz_bitmap  |                                                 |





### In this repository, we will:

- 
- 2, try to add errors\bugs\faults into graph\code, then apply delta debugging(and other SE techniques) to make everything correct again.
- 3, try to diverse single graph to set of graphs.
- 4, Generate different type of graphs and run basic algorithms on it. 






## 1,Select real dataset and run classic graph algorithms on it

In  `Basic_Algorithm.py ` , I implemented:

- `Dijkstra`, which could find out SSSP between 2 points.
-  `BFS`, which could count the size of a connected-component as well as the longest path started\ended at a point.
- `Max-flow`, which calculate max possible flow that from 2 point, here I take Dinic's method. This algorithm could also used for min-cut problem. 




## 3,Generate different set of graphs from single graph

There are 3 general ideas about how to generate new graphs.

1, Use domain-specific graph-generating pattern. Here my data is academic-relationship in physics field, so  I use 

2, Borrow graph processing ideas from existing papers.

3, Generate specific type of graph, like `part 4`

## 4,Generate different type of graphs and run basic algorithms on it. 

We will try to generate\find different types of graph and then run basic graph algorithms on them.  By doing so, we hope to find future practical research ideas\methods. 

| Graph\Algorithm       | Dijkstra(SSSP) | Size of Connected component(BFS) | Max flow(min cut) | ...  |
| --------------------- | -------------- | -------------------------------- | ----------------- | ---- |
| Original CA Road map  |                |                                  |                   |      |
| Original Relationship |                |                                  |                   |      |
| Dense                 |                |                                  |                   |      |
|                       |                |                                  |                   |      |
| Tree                  |                |                                  |                   |      |
|                       |                |                                  |                   |      |
| Connected             |                |                                  |                   |      |
|                       |                |                                  |                   |      |
| Forest                |                |                                  |                   |      |
|                       |                |                                  |                   |      |
| Pseudograph           |                |                                  |                   |      |
|                       |                |                                  |                   |      |
|                       |                |                                  |                   |      |
| ...                   |                |                                  |                   |      |













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

