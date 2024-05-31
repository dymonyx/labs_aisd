def prima_minimum_spanning_tree(graph):
    # Проверка наличия графа
    if not graph:
        return "Граф пуст"

    # Начальная вершина для построения остовного дерева
    start_node = list(graph.keys())[0]

    # Множество посещенных вершин
    visited = set(start_node)

    # Минимальное остовное дерево
    mst = []

    while len(visited) < len(graph):
        min_weight = float('inf')
        min_edge = None

        # Поиск минимального ребра среди всех ребер
        for src in visited:
            for dest, weight in graph[src]:
                if dest not in visited and weight < min_weight:
                    min_weight = weight
                    min_edge = (src, dest, weight)

        # Добавление найденного минимального ребра в остовное дерево
        if min_edge:
            mst.append(min_edge)
            visited.add(min_edge[1])
            print(visited)

    # Вычисление общего веса минимального остовного дерева
    total_weight = sum(weight for _, _, weight in mst)

    return mst, total_weight


if __name__ == '__main__':
    graph = {
        '1': [('2', 7), ('3', 15), ('4', 12), ('6', 10)],
        '2': [('1', 7), ('3', 13), ('4', 9), ('7', 8)],
        '3': [('1', 15), ('2', 13), ('4', 7), ('5', 15), ('6', 7)],
        '4': [('1', 12), ('2', 9), ('3', 7), ('5', 9), ('7', 11)],
        '5': [('3', 15), ('4', 9), ('6', 10)],
        '6': [('1', 10), ('3', 7), ('5', 10), ('7', 12)],
        '7': [('2', 8), ('4', 11), ('6', 12)]
    }

    mst, total_weight = prima_minimum_spanning_tree(graph)
    print("Минимальное остовное дерево:")
    for edge in mst:
        print(edge)
    print("Общий вес:", total_weight)
