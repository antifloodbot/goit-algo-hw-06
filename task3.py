import networkx as nx

# Створення графа
G = nx.Graph()

# Вершини (станції)
stations = [
    "Central", "North", "South", "East", "West",
    "Park", "University", "Market", "Airport", "Harbor"
]
G.add_nodes_from(stations)

# Ребра з вагами (довжини або час маршруту)
routes_with_weights = [
    ("Central", "North", 3),
    ("Central", "South", 2),
    ("Central", "East", 4),
    ("Central", "West", 6),
    ("North", "University", 5),
    ("South", "Park", 4),
    ("East", "Market", 3),
    ("West", "Market", 2),
    ("Market", "University", 1),
    ("Park", "Harbor", 6),
    ("Airport", "Harbor", 4)
]
G.add_weighted_edges_from(routes_with_weights)

# Знаходимо найкоротший шлях від кожної вершини до всіх інших
for source in stations:
    print(f"\nНайкоротші шляхи від '{source}':")
    lengths, paths = nx.single_source_dijkstra(G, source)
    for target in stations:
        if source != target:
            path_str = " → ".join(paths[target])
            print(f"  до {target:10s}: {path_str} (вартість: {lengths[target]})")