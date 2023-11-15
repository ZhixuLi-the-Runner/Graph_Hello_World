#generate a set of  graph based on single graph
# Idea one: modeling the reality: some people will born and some ppl will grow older,that is, people will meet more people but will die in certain age.
# Idea two: merge nodes with close relationship
#
import random
import networkx as nx
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

