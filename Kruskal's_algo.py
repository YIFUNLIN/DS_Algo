# Kruskal's algorithm
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):  # 定義Graph 該class的屬性
        self.V = vertices          # 有頂點
        self.graph = []            # 一個空列表，用於存儲圖形的所有邊和相對應的權重。

    def add_edge(self, u, v, w):   # u:起始頂點、v:結束頂點、w:權重
        # 將每條邊的資訊，插入到二維的Graph list中，Graph將會包含多個子列表
        self.graph.append([u, v, w])
        # eg. [[0, 1, 4], [1, 2, 2], [2, 3, 5]] 代表有3條邊，第一條是從頂點 0 到頂點 1，權重為 4 以此類推。

    # Search function
    def find(self, parent, i):  # 找出父點用，為了要實現Disjoint Set的前置作業，要判斷兩個node是否位於相同set
        if parent[i] == i:   # 若父點等於自己，就回傳自己
            return i
        return self.find(parent, parent[i])  # 父點不是自己，就recrusive 找出父點

    def apply_union(self, parent, rank, x, y):  # 會在兩個node確定是不同set後才被呼叫，做union
        # parent:是一個list，紀錄每個node的父node    rank: 該list表示每個頂點集合的深度或等級。  x 和 y: 這是我們要合併的兩個頂點
        xroot = self.find(parent, x)  # 找出兩個頂點 x 和 y 所屬set的root
        yroot = self.find(parent, y)

        # 比較兩個根的等級(高度)
        if rank[xroot] < rank[yroot]:  # 將level較小的set加到level較大的set上，以保持樹的高度盡可能小
            # 如果 x 的root 等級小於 y 的root 等級，就將 x 的root的父親設為 y 的root
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:   # 如果兩個集合的等級相同，任意一個作為新的root。
            parent[yroot] = xroot
            rank[xroot] += 1   # 相同高度tree相加，高度會多1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []  # 用來存MST的結果
        i, e = 0, 0  # 　i:索引、e:要添加到MST list的edge數量

        # Kruskal算法需要先考慮最小權重的邊，所以先依權重對所有邊進行排序。
        """
        1. self.graph: 這個屬性代表著一個二維列表，每個元素都是一個列表，代表一條邊。每條邊由三個元素組成: 起點(u), 終點(v), 和權重(w)。所以一個邊可以表示為 [u, v, w]。
        2. sorted() 函數: 這是Python的內建函數，用於對可迭代物件進行排序。
        3. key=lambda item: item[2]: 這部分指定了排序的條件。在這裡，我們需要根據每條邊的權重(w)進行排序，而權重是每條邊的第三個元素，所以我們使用索引2（因為Python的索引是從0開始的）。
        lambda是Python中的一個關鍵字，它允許我們定義一個小型無名的函數。在這裡，這個lambda函數將每條邊作為輸入（稱為item），並返回其權重作為輸出。"""
        self.graph = sorted(self.graph, key=lambda item: item[2])

        # 用來實現判斷是否為Disjoint set 與 實現Union
        parent = []  # 紀錄每個node的父點
        rank = []    # 紀錄每個 set的等級

        for node in range(self.V):  # 遍歷圖中的每個頂點
            parent.append(node)     # 先將父點初始化，將每個node的父點視為其自己的集合
            rank.append(0)          # 儲存每個set的高度，都先初始化為0(從0開始上升)

        while e < self.V - 1:        # 在MST中，邊的數量總是 V-1（V 是node的數量），會持續到我們形成 V-1 條邊為止
            u, v, w = self.graph[i]  # 從weight小到大排序好的Graph list中，一一取出邊的資訊
            i = i + 1                # 每取出一條edge就 + 1

            # 加入此edge前，要先檢查是否兩個點在相同集合，利用find()去找他們的父節點，以此來判斷是否相同
            x = self.find(parent, u)   # 每個node都會有一個父點，透過find()可得到 u 的父點
            y = self.find(parent, v)   # 會得到 v 的父點

            # 看u,v 的父點x,y是否相同
            if x != y:                                 # 若是不同set，才可加到Spanning Tree中。 相同的話要放棄，不然會形成cycle
                e = e + 1                              # 累積邊數 + 1
                result.append([u, v, w])               # u,v 為不同set時，加到spanning Tree的邊集合result中
                self.apply_union(parent, rank, x, y)   # 並將u,v所屬的集合作union

        for u, v, weight in result:                    # 遍歷result中的所有edge，印出來
            print("%d - %d: %d" % (u, v, weight))

        return result

    # 非必要
    # Add this visualization method to your Graph class
    def visualize_mst(self, mst_edges):
        G = nx.Graph()
        for u, v, weight in self.graph:
            G.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(G)
        plt.figure(figsize=(10, 6))

        # Draw all edges in light gray
        nx.draw_networkx_edges(G, pos, edge_color="gray")
        # Draw MST edges in blue
        nx.draw_networkx_edges(G, pos, edgelist=mst_edges,
                               edge_color="blue", width=2)

        # Draw nodes
        nx.draw_networkx_nodes(G, pos)
        # Draw node labels
        nx.draw_networkx_labels(G, pos)
        # Draw edge weights
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title('MST using Kruskal Algorithm')
        plt.show()


g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)


# Call the visualization method after kruskal_algo()
mst_edges = g.kruskal_algo()
g.visualize_mst(mst_edges)
