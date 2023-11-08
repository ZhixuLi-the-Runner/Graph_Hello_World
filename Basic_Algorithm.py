import heapq
from collections import deque
#Return the size of connected component
def connected_nodes(graph, node):
    if node not in graph:
        return "Node does not exist", 0

    visited = set()
    queue = deque([node])

    while queue:
        current_node = queue.popleft()
        visited.add(current_node)
        for neighbor, _ in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return visited, len(visited)

#=======================================================

def longest_path_length(graph, node):
    if node not in graph:
        return "Node does not exist", 0

    visited = set()
    queue = deque([(node, 0)])  # 将每个节点与其深度一起存储

    max_depth = 0
    while queue:
        current_node, depth = queue.popleft()
        visited.add(current_node)
        max_depth = max(max_depth, depth)  # 更新最大深度
        for neighbor, _ in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))

    return max_depth





#=======================================================

#SSSP


def dijkstra(graph, start, end):
    # 检查起始和结束节点是否存在于图中
    is_none = False
    if start not in graph:
        print("start does not exist\n")
        is_none = True
    if end not in graph:
        print("end does not exist\n")
        is_none = True

    if is_none:
        return None
    # 初始化距离字典，将所有节点的距离设置为无穷大，除了起始节点，它的距离是0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # 优先级队列将存储 (distance, node) 对
    priority_queue = [(0, start)]

    while priority_queue:
        # 从优先级队列中弹出当前最短距离的节点
        current_distance, current_node = heapq.heappop(priority_queue)

        # 如果当前节点是目标节点，返回其距离
        if current_node == end:
            return current_distance

        # 如果我们已经访问过当前节点，跳过它
        if current_distance > distances[current_node]:
            continue

        # 更新所有相邻节点的距离
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return float('infinity')  # 如果没有找到路径，返回无穷大








##=======================================================
#Max flow algorithm
#Input: undirected graph,
#Dinic algorithm
#
#
#
#
#
#
##=======================================================
class Dinic:
    def __init__(self, graph):
        self.graph = graph
        self.length = max(max(u, v) for u in graph for v, _ in graph[u]) + 1  # 获取图中最大的节点编号，并加1以确定节点数

    def bfs(self, source, sink):
        self.level = [-1] * self.length
        queue = deque([source])
        self.level[source] = 0

        while queue:
            current = queue.popleft()
            for neighbor, _ in self.graph.get(current, []):
                if self.level[neighbor] < 0 and self.residual[current][neighbor] > 0:
                    self.level[neighbor] = self.level[current] + 1
                    queue.append(neighbor)

        return self.level[sink] > 0

    def dfs(self, node, flow, sink):
        if node == sink:
            return flow
        for i in range(self.it[node], len(self.graph.get(node, []))):
            self.it[node] = i
            neighbor, capacity = self.graph[node][i]
            if self.level[neighbor] == self.level[node] + 1 and self.residual[node][neighbor] > 0:
                current_flow = min(flow, self.residual[node][neighbor])
                temp_flow = self.dfs(neighbor, current_flow, sink)
                if temp_flow > 0:
                    self.residual[node][neighbor] -= temp_flow
                    self.residual[neighbor][node] += temp_flow
                    return temp_flow
        return 0

    def max_flow(self, source, sink):
        self.residual = {u: {v: 0 for v, _ in self.graph.get(u, [])} for u in self.graph}
        for u in self.graph:
            for v, cap in self.graph[u]:
                self.residual[u][v] = cap
                if v not in self.residual:
                    self.residual[v] = {}
                if u not in self.residual[v]:  # 确保反向边也包括在残余网络中
                    self.residual[v][u] = 0

        flow = 0
        while self.bfs(source, sink):
            self.it = [0] * self.length
            current_flow = self.dfs(source, float('inf'), sink)
            while current_flow:
                flow += current_flow
                current_flow = self.dfs(source, float('inf'), sink)
        return flow





def bfs_check_connected(graph, source, sink):
    #check if there is a path from source to sink
    visited = set()
    queue = deque([source])

    while queue:
        node = queue.popleft()
        if node == sink:
            return True
        visited.add(node)
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return False


def Max_fow(graph, source, sink):
    #Run max flow algorithm on the graph and return the max flow value
    #检查source and sink是否存在于图中
    if source not in graph or sink not in graph:
        return "Source and/or sink not in the graph", 0
    # 检查源点和汇点是否连通
    if not bfs_check_connected(graph, source, sink):
        return "Source and sink not connected", 0

    # 处理无向图，将其转换成有向图
    directed_graph = {}
    for u in graph:
        for v, cap in graph[u]:
            directed_graph.setdefault(u, []).append((v, cap))
            directed_graph.setdefault(v, []).append((u, cap))  # 添加反向边

    # 计算最大流
    dinic = Dinic(directed_graph)
    return dinic.max_flow(source, sink)
