import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

adj_matrix = np.array([[0, 1, 0, 1, 1],
                       [1, 0, 1, 1, 1],
                       [0, 1, 0, 1, 1],
                       [1, 1, 1, 0, 1],
                       [1, 1, 1, 1, 0]])

# 創建一個圖
G = nx.from_numpy_array(adj_matrix)

# 計算最短路徑
path = dict(nx.all_pairs_shortest_path_length(G))

# 設定大圖的layout
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# 左側繪製圖
plt.sca(ax[0])
pos = nx.spring_layout(G)  # 對節點進行布局以便於繪圖
nx.draw(G, pos, with_labels=True, node_size=2000,
        node_color="skyblue", font_size=15, font_weight="bold")

# 右側繪製最短路徑距離矩陣
plt.sca(ax[1])
ax[1].axis("off")

# 轉換path為矩陣形式
distance_matrix = np.array(
    [[path[i][j] for j in range(len(G))] for i in range(len(G))])

# 繪製表格
the_table = plt.table(cellText=distance_matrix,
                      colLabels=[str(i) for i in range(len(G))],
                      rowLabels=[str(i) for i in range(len(G))],
                      loc='center')
the_table.auto_set_font_size(False)
the_table.set_fontsize(15)
the_table.scale(0.5, 1.5)  # 調整大小

plt.title("All pairs distances:", fontsize=15)

plt.tight_layout()
plt.show()
