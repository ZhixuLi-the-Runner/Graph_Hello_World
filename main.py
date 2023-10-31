import os
import Basic_Algorithm
import networkx as nx
import random
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

def load_aged_and_relationship_graph():
    graph = nx.Graph()

    # Load relationship graph
    with open('relationship graph.txt', 'r') as file:
        lines = file.readlines()[4:]  # Skip the header
        for line in lines:
            node1, node2 = map(int, line.strip().split('\t'))
            graph.add_edge(node1, node2)

    # Load aged graph
    aged_data = {}
    with open('Generate_graph/aged_graph.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(';')
            node_name = int(parts[0])
            degree = int(parts[1])
            neighbors = list(map(int, parts[2][1:-1].split()))
            age = int(parts[3])
            aged_data[node_name] = {'degree': degree, 'neighbors': neighbors, 'age': age}

    return graph, aged_data

# 定义各个子任务的函数
def update_ages(aged_data):
    pass


def research_interest_collaboration(graph, aged_data):
    pass


def young_scholar_activity(graph, aged_data):
    pass


def expand_collaboration_network(graph, aged_data):
    pass


def academic_conference_impact(graph, aged_data):
    pass


def new_scholars_join(graph, aged_data):
    pass


def scholar_death(graph, aged_data):
    pass


def save_updated_graphs(graph, aged_data, i):
    filename = f'timeline_{i}_.txt'
    # 保存图和年龄数据到文件
    pass


def time_pass_by():
    # 读取初始数据
    graph, aged_data = load_aged_and_relationship_graph()

    # 年龄更新
    update_ages(aged_data)

    # 研究兴趣相似的学者合作
    research_interest_collaboration(graph, aged_data)

    # 年轻学者活跃度
    young_scholar_activity(graph, aged_data)

    # 合作网络扩展
    expand_collaboration_network(graph, aged_data)

    # 学术会议和活动影响
    academic_conference_impact(graph, aged_data)

    # 新学者加入
    new_scholars_join(graph, aged_data)

    # 学者死亡
    scholar_death(graph, aged_data)

    # 输出更新
    i = 1  # 假设时间流逝了1年
    save_updated_graphs(graph, aged_data, i)




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
            time_pass_by()

        elif choice == '-1':
            return


if __name__ == '__main__':
    #main_basic_algorithms()
    main_generate_diversed_graph()
