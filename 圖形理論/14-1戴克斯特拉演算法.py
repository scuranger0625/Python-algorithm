import heapq  # 使用 Python 的 heapq 模組來實現優先佇列（最小堆）
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    """
    戴克斯特拉演算法：計算從起始點到圖中所有節點的最短路徑。

    :param graph: 圖，使用鄰接表表示，邊有權重
    :param start: 起始節點
    :return: 返回從起始點到每個節點的最短距離字典和前驅節點字典
    """
    # 1. 初始化：建立最短距離字典，起點距離為 0，其他節點為無窮大
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0  # 起始點 A 的距離為 0
    predecessors = {node: None for node in graph}  # 儲存每個節點的前驅節點

    # 2. 初始化優先佇列，初始只有起點，(當前距離, 節點)
    priority_queue = [(0, start)]  # 優先選擇最小距離的節點

    # 3. 建立一個集合來追蹤已經訪問過的節點
    visited = set()

    # 4. 開始主迴圈：當優先佇列非空時，選擇最小距離的節點
    while priority_queue:
        # 從優先佇列中取出當前距離最小的節點
        current_distance, current_node = heapq.heappop(priority_queue)

        # 如果該節點已被訪問，跳過
        if current_node in visited:
            continue

        # 5. 將當前節點標記為已訪問
        visited.add(current_node)

        # 6. 更新與當前節點相鄰的節點的距離
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight  # 計算經過當前節點到鄰居的距離

            # 如果計算出的距離比之前記錄的距離短，則更新
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                predecessors[neighbor] = current_node  # 更新前驅節點
                # 將鄰接節點加入優先佇列，以便後續處理
                heapq.heappush(priority_queue, (distance, neighbor))

    # 7. 返回最終的最短距離字典和前驅節點字典
    return shortest_distances, predecessors

def plot_graph(graph, shortest_distances, predecessors, start):
    """
    繪製圖形，並標示出從起始點到其他節點的最短路徑。
    """
    G = nx.Graph()

    # 將圖中的邊加入 NetworkX 的圖
    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    # 設置圖形佈局
    pos = nx.spring_layout(G)

    # 繪製節點和邊
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=10, font_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # 用紅色標記最短路徑上的邊
    path_edges = []
    for node, pred in predecessors.items():
        if pred is not None:
            path_edges.append((pred, node))

    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    # 顯示圖形
    plt.title(f"從節點 {start} 出發的最短路徑")
    plt.show()

# 定義圖的鄰接表，格式為 {'節點': [(鄰接節點, 邊的權重), ...]}
graph = {
    'A': [('B', 7), ('C', 2)],
    'B': [('A', 7), ('C', 2), ('D', 5), ('E', 6)],
    'C': [('A', 2), ('B', 2), ('D', 4)],
    'D': [('B', 5), ('C', 4), ('E', 3), ('G', 2)],
    'E': [('B', 6), ('D', 3), ('F', 2)],
    'F': [('E', 2), ('G', 3)],
    'G': [('D', 2), ('F', 3)]
}

# 從節點 A 開始計算到其他節點的最短路徑
distances, predecessors = dijkstra(graph, 'A')

# 打印最終結果
print("從節點 A 到各節點的最短距離:")
for node, distance in distances.items():
    print(f"節點 {node}: {distance}")

# 繪製圖形並標示最短路徑
plot_graph(graph, distances, predecessors, 'A')
