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
import heapq

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
