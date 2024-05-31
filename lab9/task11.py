def dijkstra(graph, start, end, extra_paths):
    # Словарь для хранения дистанций от начальной вершины до остальных
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Словарь для отслеживания предыдущих вершин
    previous = {vertex: None for vertex in graph}

    # Множество для хранения посещенных вершин
    visited = set()

    while True:
        # Найти вершину с наименьшей дистанцией, которая еще не посещена
        min_distance = float('inf')
        min_vertex = None
        for vertex in graph:
            if distances[vertex] < min_distance and vertex not in visited:
                min_distance = distances[vertex]
                min_vertex = vertex

        # Если все вершины посещены или нет пути до конечной вершины, выйти из цикла
        if min_vertex is None or min_vertex == end:
            break

        # Посетить текущую вершину
        visited.add(min_vertex)

        # Обновить дистанции до соседних вершин
        for neighbor, weight in graph[min_vertex].items():
            distance = distances[min_vertex] + weight

            # Проверка на использование дополнительных путей
            if (min_vertex, neighbor) in extra_paths:
                if extra_paths[(min_vertex, neighbor)] <= 0:
                    continue
                extra_paths[(min_vertex, neighbor)] -= 1

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = min_vertex

    # Восстановление пути из предыдущих вершин
    path = []
    if distances[end] != float('inf'):
        current_vertex = end
        while current_vertex is not None:
            prev_vertex = previous[current_vertex]
            if prev_vertex is not None:
                path.append((prev_vertex, current_vertex))
            current_vertex = prev_vertex
        path.reverse()

    return distances[end], path


if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    extra_paths = {
        ('B', 'D'): 1,
        ('C', 'D'): 1
    }

    extra_paths2 = {
        ('B', 'D'): 1,
        ('C', 'D'): 0
    }

    start_vertex = 'A'
    end_vertex = 'D'

    shortest_distance, path = dijkstra(graph, start_vertex, end_vertex, extra_paths)
    print(f"Самый короткий путь между вершинами {start_vertex} и {end_vertex} равен {shortest_distance}")
    print(f"Состав рёбер минимального пути: {path}")

    shortest_distance, path = dijkstra(graph, start_vertex, end_vertex, extra_paths2)
    print(f"Самый короткий путь между вершинами {start_vertex} и {end_vertex} равен {shortest_distance}")
    print(f"Состав рёбер минимального пути: {path}")
