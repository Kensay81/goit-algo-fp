import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4())  

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, with_labels=True)
    plt.show()

def dfs(root):
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        if node:
            order.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return order

def bfs(root):
    queue = [root]
    order = []
    while queue:
        node = queue.pop(0)
        if node:
            order.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return order

def update_colors(order):
    n = len(order)
    for i, node in enumerate(order):
        intensity = int(255 * i / (n - 1)) if n > 1 else 0
        hex_intensity = f'{intensity:02x}'
        node.color = f'#{hex_intensity}ff{hex_intensity}'


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.left.left.left = Node(11)
root.left.left.right = Node(12)
root.left.right.left = Node(13)
root.left.right.right = Node(14)
root.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
root.right.right.left = Node(9)
root.right.right.right = Node(2)

# Обхід в глибину (DFS)
dfs_order = dfs(root)
update_colors(dfs_order)
draw_tree(root)

# Обхід в ширину (BFS)
bfs_order = bfs(root)
update_colors(bfs_order)
draw_tree(root)
