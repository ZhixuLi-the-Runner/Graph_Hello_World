import Basic_Algorithm

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


def display_menu():
    print("请选择一个选项：")

    print("1. 查询连接节点总数")
    print("2. 查询最长半径长度")
    print("3. 查询最两点间短路径长度")
    print("0. 退出")


def main():
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


if __name__ == '__main__':
    main()
