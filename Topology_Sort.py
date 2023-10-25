import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict  # 有包好的資料結構


class Graph:
    def __init__(self, vertices):  # 類別初始化
        self.adjacencyList = defaultdict(list)  # 相鄰列表，用於儲存邊
        self.vertices = vertices  # 　儲存圖的節點數
        self.visited = [False] * vertices  # 使用bool值=False，來記錄DFS所訪問過的node
        self.stack = []  # 儲存Topology Sort完的結果
        self.G = nx.DiGraph()  # 是 networkx 的有向圖物件，將用它來畫圖

    def createEdge(self, u, v):  # 目的是在圖中添加一條邊，從節點 u 指向節點 v
        # 將node v 添加到node u 的adjacent list中。代表圖中會存在一條從 u 到 v 的邊
        self.adjacencyList[u].append(v)
        self.G.add_edge(u, v)  # 　視覺化用，將邊(u, v)添加到 networkx 的圖中

    def dfs(self, v):   # 先定義DFS，等等要給Topology Sort使用
        self.visited[v] = True   # 將拜訪的該點先設為True

        for i in self.adjacencyList[v]:  # 遍歷該點v的所有相鄰節點
            if not self.visited[i]:  # 若有相鄰節點未被訪問
                self.dfs(i)  # Recrusive，訪問他!

        self.stack.insert(0, v)
        # 使用模仿stack 的行為，但透過insert(0, v)以確保最後完成DFS的節點在拓撲排序中的位置是正確的。如果使用 append，那麼在返回拓撲排序結果之前，我們還需要反轉這個列表
        # 使用 self.stack.insert(0, v)，會將節點 v 放在 "堆疊" 的最底部（也就是list的開頭）。隨著更多的節點完成DFS，它們會持續被放到這個 "堆疊" 的最底部。
        # 所以，最後當DFS完成，self.stack 的第一個元素（也就是最底部）是最後一個完成DFS的節點，而最後一個元素（也就是最頂部）是第一個完成DFS的節點。
        # 這是拓撲排序的核心步驟，因為最依賴於所有其他節點的節點，應該先被處理。所以把它插入到list前端

    def topologicalSort(self):
        for i in range(self.vertices):  # 遍歷Graph中所有點
            if not self.visited[i]:  # 檢查節點 i 是否已被訪問
                self.dfs(i)          # 如果還沒有，則執行 DFS
        return self.stack            # 返回結果堆疊，這是拓撲排序的結果。

    def drawGraph(self):
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_size=700, node_color="skyblue",
                font_size=15, font_weight='bold', width=2.0, edge_color="gray")
        plt.title("Directed Acyclic Graph (DAG)")
        plt.show()


# 測試
G = Graph(6)
G.createEdge(0, 1)
G.createEdge(0, 2)
G.createEdge(1, 3)
G.createEdge(1, 5)
G.createEdge(2, 3)
G.createEdge(2, 5)
G.createEdge(3, 4)
G.createEdge(5, 4)
print("Topological Sort Order:", G.topologicalSort())
G.drawGraph()
