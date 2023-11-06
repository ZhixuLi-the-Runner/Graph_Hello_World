def convert_to_dense(graph):
    # Your implementation here
    # 如果无法转换为密集图，返回原始图
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

