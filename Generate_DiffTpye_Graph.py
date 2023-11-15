import random
import heapq
from collections import deque
import os
import matplotlib.pyplot as plt
import networkx as nx


def save_original_graph(graph, file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            for node, edges in graph.items():
                for edge in edges:
                    file.write(f"{node} {edge[0]} {edge[1]}\n")


def save_processed_graph(graph, file_path):
    with open(file_path, "w") as file:
        for node, edges in graph.items():
            for edge in edges:
                file.write(f"{node} {edge[0]} {edge[1]}\n")


def print_partial_graph(graph, num_nodes_to_print=5):
    print("Partial view of the generated graph:")
    for node, edges in list(graph.items())[:num_nodes_to_print]:
        print(f"Node {node}: {edges}")
def convert_to_dense(graph):
    print("Converting to dense graph...")
    nodes = list(graph.keys())
    num_nodes = len(nodes)

    # 确保 graph 是双向的，如果不是，这里需要处理
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            # 以70%的概率添加边，如果这条边还不存在的话
            if random.random() < 0.7:
                # 添加带权重的边 (i, j)，权重为1
                graph[nodes[i]].append((nodes[j], 1))  # 将邻接节点改为元组，包含节点和权重
                # 对于无向图，还需要添加边 (j, i)
                graph[nodes[j]].append((nodes[i], 1))  # 同上
                # print(f"Adding edge ({nodes[i]}, {nodes[j]})")
    #
    # # 确保没有重复的边并移除可能的自环
    # for node, edges in graph.items():
    #     # 如果允许自环，那么下面的去重操作需要调整
    #     unique_edges = set()
    #     for edge in edges:
    #         if edge[0] != node:  # 排除自环
    #             unique_edges.add(edge)
    #     graph[node] = list(unique_edges)
    #print_partial_graph(graph)
    return graph


def convert_to_sparse(graph):
    # Your implementation here
    # 如果无法转换为稀疏图，返回原始图
    return graph

def convert_to_tree(graph):
    # 初始化一个空的树
    tree = {node: [] for node in graph}
    # 选择图中的任意一个节点作为起始节点
    start_node = next(iter(graph))
    # 创建一个优先队列，用于选择最小权重的边
    edges = [(0, start_node, None)]  # (权重, 目标节点, 源节点)
    # 创建一个集合，用于跟踪已经被添加到树中的节点
    in_tree = set()

    while edges:
        # 选择最小权重的边
        weight, node, parent = heapq.heappop(edges)
        # 如果这个节点已经在树中，则跳过
        if node in in_tree:
            continue
        # 将节点添加到树中
        in_tree.add(node)
        # 如果这个节点不是起始节点，那么将边添加到树中
        if parent is not None:
            tree[parent].append((node, weight))
            tree[node].append((parent, weight))
        # 将所有与这个节点相连的边添加到优先队列中
        for neighbour, weight in graph[node]:
            if neighbour not in in_tree:
                heapq.heappush(edges, (weight, neighbour, node))

    # for node, edges in tree.items():
    #     print(f"{node}: {edges}")
    return tree


def convert_to_forest(graph):
    # 初始化森林
    forest = {node: [] for node in graph}
    # 用于追踪哪些节点已经在森林中
    visited = set()

    # 对图中的每个节点进行遍历
    for start_node in graph:
        # 如果节点已经被访问，则跳过
        if start_node in visited:
            continue
        # 运行普里姆算法
        edges = [(0, start_node, None)]  # (权重, 目标节点, 源节点)
        in_tree = set()

        while edges:
            weight, node, parent = heapq.heappop(edges)
            if node in in_tree:
                continue
            in_tree.add(node)
            visited.add(node)

            if parent is not None:
                forest[parent].append((node, weight))
                forest[node].append((parent, weight))

            for neighbour, weight in graph[node]:
                if neighbour not in in_tree:
                    heapq.heappush(edges, (weight, neighbour, node))

    return forest


def convert_to_Pseudograph(graph):
    pseudo_graph = {node: list(edges) for node, edges in graph.items()}  # 复制原始图

    for node, edges in pseudo_graph.items():
        # 以50%的概率添加一个指向自己的边（自环）
        if random.random() < 0.5:
            edges.append((node, 1))  # 假设权重为1

        # 遍历每个邻接节点，以50%的概率添加一条同等权重的边（多重边）
        for neighbor, weight in edges:
            if neighbor != node and random.random() < 0.5:  # 避免自环被重复添加
                edges.append((neighbor, weight))
    #for node, edges in pseudo_graph.items():
    #    print(f"{node}: {edges}")
    # 因为添加了多重边，所以不需要去重
    return pseudo_graph




def get_connected_components(graph):
    # 用于存储所有连通分量的列表
    components = []
    # 用于标记节点是否已被访问
    visited = set()

    for node in graph:
        if node not in visited:
            # 开始一个新的连通分量
            component = []
            # 创建一个队列用于宽度优先搜索
            queue = deque([node])
            # 开始宽度优先搜索
            while queue:
                current = queue.popleft()
                if current not in visited:
                    visited.add(current)
                    component.append(current)
                    # 将邻接的未访问节点加入队列
                    for neighbour, _ in graph[current]:
                        if neighbour not in visited:
                            queue.append(neighbour)
            # 添加连通分量到列表中
            components.append(component)

    return components

def connect_components(components, graph):
    # 遍历连通分量，将它们通过添加边相连
    for i in range(len(components) - 1):
        # 连接每个连通分量的第一个节点到下一个连通分量的第一个节点
        graph[components[i][0]].append((components[i+1][0], 1))  # 假设新添加的边权重为1
        graph[components[i+1][0]].append((components[i][0], 1))  # 因为是无向图，所以需要添加双向边

def convert_to_connected(graph):
    # 获取图的所有连通分量
    components = get_connected_components(graph)
    # 如果只有一个连通分量，那么图已经是连通的
    if len(components) > 1:
        # 连接所有连通分量
        connect_components(components, graph)
    return graph


def build_graph(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line[0] != '#' and line.strip():  # 跳过注释行和空行
                parts = line.strip().split()
                from_node, to_node = map(int, parts[:2])
                weight = int(parts[2]) if len(parts) > 2 else 1#默认权重为1
                graph.setdefault(from_node, []).append((to_node, weight))
                graph.setdefault(to_node, []).append((from_node, weight))  # 为无向图添加反向边
    return graph


def display_graph(file_path):
    # 创建一个空的图形
    G = nx.Graph()
    print("drawing graph...")
    # 从文件中读取图形数据
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                from_node, to_node, weight = map(int, parts)
                G.add_edge(from_node, to_node, weight=weight)

    # 绘制图形
    pos = nx.spring_layout(G)  # 定义一个布局
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='black')

    # 显示边的权重
    #edge_labels = nx.get_edge_attributes(G, 'weight')
    #nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # 显示图形
    plt.show()


def Generate_graphs(graph_type, file_path,table):
    # Read the original graph from the file
    graph = build_graph(file_path)

    save_original_graph(graph, r"Generate_graph\original_graph.txt")
    # Convert the graph based on the specified graph type

    if graph_type == 'dense':
        new_graph = convert_to_dense(graph)
    elif graph_type == 'original':
        new_graph = graph
    elif graph_type == 'sparse ':
        new_graph = convert_to_sparse(graph)
    elif graph_type == 'tree':
        new_graph = convert_to_tree(graph)
    elif graph_type == 'forest':
        new_graph = convert_to_forest(graph)
    elif graph_type == 'Pseudograph':
        new_graph = convert_to_Pseudograph(graph)
    elif graph_type == 'connected':
        new_graph = convert_to_connected(graph)
    else:
        raise ValueError(f"Unknown graph type: {graph_type}")
    save_processed_graph(new_graph, fr"Generate_graph\{table}_{graph_type}.txt")
    # Optionally, return the new graph or write it to a file

    #display_graph(fr"Generate_graph\{table}_{graph_type}.txt")
    return new_graph




# Example usage:
#new_graph = Generate_graphs('dense', 'path_to_your_file.txt')

