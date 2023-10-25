adjacency_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}


def BFS(start_vertex):
    visited = set()
    queue = [start_vertex]  # 利用list可實現Queue
    while queue:
        vertex = queue.pop(0)  # FIFO 利用pop(0)取出最前端元素
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(
                neighbor for neighbor in adjacency_list[vertex] if neighbor not in visited)


BFS('A')
