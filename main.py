import os
import Basic_Algorithm
import Generate_diversed_graph
import random
import time
import memory_profiler
import Generate_DiffTpye_Graph

debug = False


def build_graph(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line[0] != '#' and line.strip():  # 跳过注释行和空行
                parts = line.strip().split()
                from_node, to_node = map(int, parts[:2])
                weight = int(parts[2]) if len(parts) > 2 else 1
                graph.setdefault(from_node, []).append((to_node, weight))
                graph.setdefault(to_node, []).append((from_node, weight))  # 为无向图添加反向边
    return graph

def build_graph_gengra(file_path):
    G = nx.Graph()  # 创建一个空的无向图
    with open(file_path, 'r') as file:
        lines = file.readlines()[4:]  # 跳过前四行的文件头
        for line in lines:
            node1, node2 = map(int, line.strip().split('\t'))
            if G.has_edge(node1, node2):
                G[node1][node2]['weight'] += 1
            else:
                G.add_edge(node1, node2, weight=1)

    # 创建目录并保存图
    os.makedirs('Generate_graph', exist_ok=True)
    nx.write_weighted_edgelist(G, 'Generate_graph/weighted_graph.txt')
    return G
#===================================================================================================

def display_menu():
    print("请选择一个选项：")

    print("1. 查询连接节点总数")
    print("2. 查询最长半径长度")
    print("3. 查询最两点间短路径长度")
    print("0. 退出")

def display_menu_gg():
    print("请选择一个选项：")

    print("1. Initialize aged graph")
    print("2. mutate aged graph")
    print("3. let time pass by")
    print("0. 退出")
#===================================================================================================

def main_basic_algorithms():
    graph = None  # 初始化图为 None
    file_path = 'relationship graph.txt'
    graph = build_graph(file_path)
    while True:
        display_menu()  # 显示菜单
        choice = input("请输入你的选择：")
        if choice == '-1':
            return


        elif choice == '1':
            if graph is None:
                print("请先构建图。")
                continue
            try:
                node = int(input("请输入节点序号："))
            except ValueError:
                print("请输入有效的节点编号。")
                continue
            connected, num_connected = Basic_Algorithm.connected_nodes(graph, node)
            if isinstance(connected, str):
                print(connected)
            else:
                print(f'与节点 {node} 直接或间接连接的节点总数是 {num_connected}')
        elif choice == '2':
            if graph is None:
                print("请先构建图。")
                continue
            try:
                node = int(input("请输入节点序号："))
            except ValueError:
                print("请输入有效的节点编号。")
                continue
            longest_distance = Basic_Algorithm.longest_path_length(graph, node)
            if isinstance(longest_distance, str):
                print(longest_distance)
            else:
                print(f'以节点 {node} 为中心的半径长度是 {longest_distance}')
        elif choice == '3':
            if graph is None:
                print("请先构建图。")
                continue
            try:
                start_node = int(input("请输入起点："))
                end_node = int(input("请输入终点："))
            except ValueError:
                print("请输入有效的节点编号。")
                continue
            shortest_distance = Basic_Algorithm.dijkstra(graph, start_node, end_node)
            if shortest_distance == float('infinity'):
                print(f'没有找到从节点 {start_node} 到节点 {end_node} 的路径。')
            else:
                print(f'节点 {start_node} 和节点 {end_node} 之间的最短路径长度是 {shortest_distance}')
        elif choice == '0':
            break  # 退出循环，结束程序
        else:
            print("无效的选择，请重新输入。")

#---------------------------------------------
def calculate_degree(graph, node):
    return graph.degree(node, weight='weight')

def find_kth_largest_degree(graph, k):
    degrees = [d for n, d in graph.degree(weight='weight')]
    return quickselect(degrees, 0, len(degrees)-1, k)

def quickselect(arr, low, high, k):
    if low <= high:
        pi = partition(arr, low, high)
        if pi == k:
            return arr[pi]
        elif pi < k:
            return quickselect(arr, pi + 1, high, k)
        else:
            return quickselect(arr, low, pi - 1, k)
    return -1

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def assign_age_and_get_adj_list(graph, threshold_degree):
    adjacency_list = []
    for node in graph.nodes:
        degree = calculate_degree(graph, node)
        neighbors = list(graph.neighbors(node))
        is_big_fish = degree >= threshold_degree
        age = random.randint(30, 70) if is_big_fish else random.randint(20, 60)
        graph.nodes[node]['age'] = age
        adjacency_list.append(f"{node} {degree} [{' '.join(map(str, neighbors))}] {age}")
    return adjacency_list

#===================================================================================================

#===================================================================================================

def main_generate_diversed_graph():
    graph = None  # 初始化图为 None
    file_path = 'relationship graph.txt'
    graph = build_graph_gengra(file_path)
    while True:
        display_menu_gg()
        choice = input("请输入你的选择：")
        if choice == '1':
            total_nodes = len(graph.nodes)
            threshold_degree = find_kth_largest_degree(graph, total_nodes * 3 // 10)
            adjacency_list = assign_age_and_get_adj_list(graph, threshold_degree)
            with open('Generate_graph/aged_graph.txt', 'w') as file:
                file.write('\n'.join(adjacency_list))

        elif choice == '2':
            None;
        elif choice == '3':
            Generate_diversed_graph.time_pass_by()

        elif choice == '-1':
            return


def main_BasicAlgOn_DiffG():
# ===================================================================================================
# 1, Explore different features of the graphs
# 2, Generate\Find graph with different features
# 3, Run Basic algorithms on different graphs and test the performance
# ===================================================================================================
    graph_types = ['dense', 'sparce ','tree', 'forrest',]  # Replace with actual graph types or features


    print("\nPlease input the start node and end node for Relationship Graph:")
    start = int(input())
    end = int(input())
    path='Original_data\\relationship_graph.txt'
    for graph_type in graph_types:
        print(f"Generating {graph_type} graph...")
        graph = Generate_DiffTpye_Graph.Generate_graphs(graph_type)  # Replace with the actual function to generate graphs
        #print(f"Running Dijkstra's algorithm on {graph_type} graph...\n")
        ##----------------------------------------------------------------------
        # Run Dijkstra's algorithm and measure time and mem usage
        start_time = time.time()
        result = Basic_Algorithm.dijkstra(graph, start, end)  # Assuming dijkstra is the function to run
        elapsed_time = time.time() - start_time
        print(f"Shortest path length: {result}\n")
        print(f"Time taken: {elapsed_time:.2f} seconds")

        # Measure memory usage (optional)
        mem_usage = memory_profiler.memory_usage((Basic_Algorithm.dijkstra, (graph,)))
        print(f"Memory used: {mem_usage[0]:.2f} MiB")

##----------------------------------------------------------------------

    print("\nPlease input the start node and end node for Road Graph:")
    start = int(input())
    end = int(input())
    path='Filtered_data\\roadNet-CA_filtered.txt'
    for graph_type in graph_types:
        print(f"Generating {graph_type} graph...")
        graph = Generate_DiffTpye_Graph.Generate_graphs(graph_type,path)  # Replace with the actual function to generate graphs
        # print(f"Running Dijkstra's algorithm on {graph_type} graph...\n")
        ##----------------------------------------------------------------------
        # Run Dijkstra's algorithm and measure time and mem usage
        start_time = time.time()
        result = Basic_Algorithm.dijkstra(graph, start, end)  # Assuming dijkstra is the function to run
        elapsed_time = time.time() - start_time
        print(f"Shortest path length: {result}\n")
        print(f"Time taken: {elapsed_time:.2f} seconds")

        # Measure memory usage (optional)
        mem_usage = memory_profiler.memory_usage((Basic_Algorithm.dijkstra, (graph,)))
        print(f"Memory used: {mem_usage[0]:.2f} MiB")













if __name__ == '__main__':
    #main_basic_algorithms()
    #main_generate_diversed_graph()

    main_BasicAlgOn_DiffG()
    print("Done!")
