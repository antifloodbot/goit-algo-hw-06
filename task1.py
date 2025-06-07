import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф
G = nx.Graph()

# Додаємо вершини (станції)
stations = [
    "Central", "North", "South", "East", "West",
    "Park", "University", "Market", "Airport", "Harbor"
]
G.add_nodes_from(stations)

# Додаємо ребра (маршрути між станціями)
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

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, with_labels=True, node_color="lightblue", node_size=1500, font_size=12)
plt.title("City Transport Network Graph")
plt.axis("off")
plt.show()

# Аналіз характеристик графа
print("Кількість вершин (станцій):", G.number_of_nodes())
print("Кількість ребер (маршрутів):", G.number_of_edges())

degrees = dict(G.degree())
print("\nСтупінь кожної вершини:")
for station, degree in degrees.items():
    print(f"{station}: {degree}")