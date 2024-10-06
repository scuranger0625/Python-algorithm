import matplotlib.pyplot as plt
import networkx as nx

def dfs_iterative_draw(graph, start):
    """
    使用堆疊進行深度優先搜尋（DFS）的迭代實現，並動態繪製圖形。
    
    :param graph: 圖，使用鄰接表表示
    :param start: 起始節點
    """
    # 使用 NetworkX 構建圖
    G = nx.Graph(graph)

    # 初始化堆疊並將起始節點推入
    stack = [start]
    # 初始化訪問集合，用來追蹤已訪問的節點
    visited = set()

    # 初始化繪圖佈局
    pos = nx.spring_layout(G)  # 為節點生成佈局
    plt.figure(figsize=(8, 6))

    # 當堆疊不為空時，繼續遍歷
    while stack:
        # 從堆疊中取出當前節點
        node = stack.pop()  # 從堆疊頂部取出節點（先進後出）

        # 如果節點還沒有被訪問，進行以下操作
        if node not in visited:
            # 標記節點為已訪問
            visited.add(node)
            print(f"訪問節點: {node}")  # 打印當前訪問的節點

            # 繪製當前圖形狀態，已訪問節點顯示為紅色
            plt.clf()  # 清除前一次繪圖
            node_colors = ['red' if n in visited else 'lightblue' for n in G.nodes()]  # 設置顏色
            nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10, font_color='black')
            plt.pause(0.5)  # 暫停 0.5 秒，以便查看動態變化

            # 將當前節點的鄰接節點推入堆疊
            # 這裡使用 reversed 是為了確保節點按順序被訪問
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    # 結束後繪製最終的結果
    plt.show()


# 定義圖的鄰接表表示法
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 執行 DFS 迭代搜尋並繪製圖形
dfs_iterative_draw(graph, 'A')
