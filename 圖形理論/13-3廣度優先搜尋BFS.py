import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

def bfs_draw(graph, start):
    """
    廣度優先搜尋（BFS）並繪製圖形。
    當每個節點被訪問時，動態更新圖形顯示 BFS 過程。
    
    :param graph: 圖，使用鄰接表表示
    :param start: 起始節點
    """
    # 使用 NetworkX 構建圖
    G = nx.Graph(graph)

    # 初始化 BFS 隊列和訪問集
    queue = deque([start])
    visited = set([start])

    # 初始化繪圖
    pos = nx.spring_layout(G)  # 為節點生成佈局
    plt.figure(figsize=(8, 6))
    
    # 遍歷隊列
    while queue:
        node = queue.popleft()  # 取出當前節點
        print(f"訪問節點: {node}")
        
        # 動態更新圖，標記已訪問的節點為紅色
        plt.clf()  # 清除上一個圖
        nx.draw(G, pos, with_labels=True, node_color=['red' if n in visited else 'lightblue' for n in G.nodes()])
        plt.pause(0.5)  # 暫停一段時間來顯示變化

        # 處理與當前節點相連的鄰接節點
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # 最終繪製完成的圖
    plt.show()

# 定義圖的鄰接表
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 執行 BFS 並繪製圖形
bfs_draw(graph, 'A')
