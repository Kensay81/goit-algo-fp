import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Обласні центри України та їх наближені до реальних координати
cities_coords = {
    "Київ": (30.52, 50.45),
    "Харків": (36.25, 49.98),
    "Дніпро": (35.04, 48.45),
    "Одесса": (30.73, 46.48),
    "Львів": (24.03, 49.84),
    "Запоріжжя": (35.18, 47.84),
    "Кривий Ріг": (33.35, 47.91),
    "Кропивницький": (32.16, 48.30),
    "Миколаїв": (31.98, 46.97),
    "Маріуполь": (37.53, 47.10),
    "Вінниця": (28.48, 49.23),
    "Херсон": (32.62, 46.63),
    "Чернігів": (31.29, 51.50),
    "Полтава": (34.53, 49.58),
    "Черкаси": (32.06, 49.44),
    "Суми": (34.80, 50.91),
    "Рівно": (26.25, 50.62),
    "Хмельницький": (26.98, 49.42),
    "Чернівці": (25.94, 48.29),
    "Житомир": (28.65, 50.25),
    "Тернопіль": (25.59, 49.55),
    "Луцьк": (25.33, 50.74),
    "Івано-Франківськ": (24.71, 48.92),
    "Ужгород": (22.30, 48.62),
    "Луганськ": (39.30, 48.57),
    "Донецьк": (37.80, 48.00),
    "Сімферополь": (34.11, 44.95),
}

# Відстань (майже всюди взяв з гугл мапс реальну відстань)
edges = [
    ("Київ", "Харків", 479),
    ("Київ", "Одесса", 476),
    ("Київ", "Дніпро", 480),
    ("Київ", "Черкаси", 192),
    ("Київ", "Вінниця", 246),
    ("Київ", "Житомир", 139),
    ("Київ", "Чернігів", 155),
    ("Київ", "Полтава", 350),
    ("Київ", "Суми", 332),
    ("Житомир", "Рівно", 190),
    ("Рівно", "Луцьк", 73),
    ("Рівно", "Львів", 211),
    ("Львів", "Луцьк", 152),
    ("Львів", "Тернопіль", 127),
    ("Львів", "Івано-Франківськ", 135),
    ("Львів", "Ужгород", 248),
    ("Ужгород", "Івано-Франківськ", 270),
    ("Чернівці", "Івано-Франківськ", 135),
    ("Тернопіль", "Івано-Франківськ", 132),
    ("Тернопіль", "Хмельницький", 112),
    ("Тернопіль", "Рівно", 154),
    ("Вінниця", "Хмельницький", 119),
    ("Вінниця", "Чернівці", 284),
    ("Вінниця", "Житомир", 153),
    ("Вінниця", "Кропивницький", 321),
    ("Вінниця", "Одесса", 425),
    ("Харків", "Дніпро", 213),
    ("Дніпро", "Запоріжжя", 70),
    ("Дніпро", "Кривий Ріг", 146),
    ("Дніпро", "Донецьк", 249),
    ("Дніпро", "Черкаси", 321),
    ("Одесса", "Миколаїв", 135),
    ("Миколаїв", "Херсон", 67),
    ("Миколаїв", "Кривий Ріг", 175),
    ("Миколаїв", "Кропивницький", 183),
    ("Кривий Ріг", "Кропивницький", 119),
    ("Дніпро", "Полтава", 197),
    ("Полтава", "Харків", 143),
    ("Полтава", "Суми", 176),
    ("Черкаси", "Кропивницький", 129),
    ("Харків", "Суми", 186),
    ("Харків", "Донецьк", 336),
    ("Харків", "Луганськ", 339),
    ("Херсон", "Сімферополь", 267),
    ("Херсон", "Маріуполь", 423),
    ("Донецьк", "Луганськ", 155),
    ("Донецьк", "Маріуполь", 121),
    ("Запоріжжя", "Маріуполь", 239),
]

G = nx.Graph()

for city, (x, y) in cities_coords.items():
    G.add_node(city, pos=(x, y))

for city1, city2, distance in edges:
    G.add_edge(city1, city2, weight=distance)

pos = nx.get_node_attributes(G, 'pos')

plt.figure(figsize=(15, 10))
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.grid(True)
plt.title("Граф областних центрів и крупних міст України та автомобільних шляхів між ними")
plt.show()

# Реалізація алгоритму Дейкстри з використанням бінарної купи
def dijkstra(graph, start):
    # Ініціалізація
    pq = []  # Пріоритетна черга
    heapq.heappush(pq, (0, start))  # Відстань до стартового вузла = 0
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    previous_nodes = {node: None for node in graph.nodes}
    shortest_path_tree = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node in shortest_path_tree:
            continue

        shortest_path_tree.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes

# Виклик алгоритму Дейкстри
start_city = "Київ"
distances, previous_nodes = dijkstra(G, start_city)

# Виведення найкоротших шляхів від стартового міста до кожного іншого
def get_shortest_path(previous_nodes, start, target):
    path = []
    while target:
        path.append(target)
        target = previous_nodes[target]
    path.reverse()
    return path

print(f"Найкоротші шляхи від {start_city} до інших міст з довжинами:")
for city in G.nodes:
    if city != start_city:
        path = get_shortest_path(previous_nodes, start_city, city)
        path_str = " -> ".join(path)
        print(f"{city}: {path_str}, Довжина: {distances[city]}")
