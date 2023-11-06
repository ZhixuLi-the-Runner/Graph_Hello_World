import random

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
    print_partial_graph(graph)
    return graph


def convert_to_sparse(graph):
    # Your implementation here
    # 如果无法转换为稀疏图，返回原始图
    return graph

def convert_to_tree(graph):
    # Your implementation here
    # 如果无法转换为树，返回原始图
    return graph

def convert_to_forest(graph):
    # Your implementation here
    # 如果无法转换为森林，返回原始图
    return graph

def convert_to_Pseudograph(graph):
    # Your implementation here
    # 如果无法转换为伪图，返回原始图
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

def Generate_graphs(graph_type, file_path):
    # Read the original graph from the file
    graph = build_graph(file_path)


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
    else:
        raise ValueError(f"Unknown graph type: {graph_type}")

    # Optionally, return the new graph or write it to a file
    return new_graph




# Example usage:
#new_graph = Generate_graphs('dense', 'path_to_your_file.txt')

