# task2.py
import networkx as nx
from collections import deque

# Побудова графа з завдання 1
G = nx.Graph()
stations = [
    "Central", "North", "South", "East", "West",
    "Park", "University", "Market", "Airport", "Harbor"
]
G.add_nodes_from(stations)
routes = [
    ("Central", "North"),
    ("Central", "South"),
    ("Central", "East"),
    ("Central", "West"),
    ("North", "University"),
    ("South", "Park"),
    ("East", "Market"),
    ("West", "Market"),
    ("Market", "University"),
    ("Park", "Harbor"),
    ("Airport", "Harbor")
]
G.add_edges_from(routes)

# DFS: пошук шляху у глибину
def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        vertex, path = stack.pop()
        if vertex == goal:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in reversed(list(graph.neighbors(vertex))):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

# BFS: пошук шляху в ширину
def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        vertex, path = queue.popleft()
        if vertex == goal:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.neighbors(vertex):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

# Знайдемо шлях від "Central" до "Harbor"
start, goal = "Central", "Harbor"
dfs_result = dfs_path(G, start, goal)
bfs_result = bfs_path(G, start, goal)

# Вивід
print("🔍 Шлях DFS:", " → ".join(dfs_result))
print("🔍 Шлях BFS:", " → ".join(bfs_result))

# Порівняння
print("\n📌 Пояснення:")
print("DFS шукає шлях у глибину, тому може пройти довший маршрут перед тим, як знайде ціль.")
print("BFS шукає в ширину, тому завжди знаходить найкоротший шлях (за кількістю станцій).")