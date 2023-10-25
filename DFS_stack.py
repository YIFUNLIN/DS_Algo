def dfs(start_vertex, graph_dict):
    visited = set()   # 使用集合來保存已訪問的節點
    stack = [start_vertex]  # python的list可做為stack

    while stack:  # 當堆疊不為空時
        vertex = stack.pop()   # pop()掉最上面的node
        if vertex is not visited:  # 如果這個節點還未訪問
            print(vertex, end=" ")  # 印出來
            visited.add(vertex)     # 並標記加入到訪問過的set中
            stack.extend(graph_dict[vertex])  # 先對該node的鄰居全都丟入stack，後續會再處理
            # 利用list.extend()用於將一個list（或任何可迭代對象）的所有元素添加到另一個list的末端
            # 因為是while loop 再回去前面一一pop 檢視是否visited過了


# 測試 dfs_stack 函數
graph_dict = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
dfs('A', graph_dict)
