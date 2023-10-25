visited = set()  # 建立一個初始化集合
graph_dict = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def dfs(vertex):  # vertex為目標走訪值
    global visited, graph_dict  # 當一個區域變數要修改全域變數的值時，要宣告為Global variable才能真正修改
    if vertex in visited:  # 如果當前節點已經被訪問過（即它已經在 visited 集合中）
        return visited    # 則回傳 visited 集合
    visited.add(vertex)   # 若當前節點尚未被訪問，則將其添加到 visited 集合中
    print(vertex, end=" ")   # 印出該點

    # 要去拜訪vertex的鄰居們，利用vertex去比對dict的key，當有找到時就回傳該列表
    for neighbor in graph_dict[vertex]:
        # neighbor會走訪該列表內的node
        if neighbor not in visited:  # 若該點未被拜訪過，則代表它不在visited集合內
            dfs(neighbor)            # 對它做 dfs 去拜訪他
    return visited


# 測試 dfs 函數
dfs('A')
