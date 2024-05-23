import uuid
import networkx as nx
import matplotlib.pyplot as plt

class MaxHeapNode:
    def __init__(self, key, color="lightblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4()) 

def add_heap_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_heap_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_heap_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_max_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_heap_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}  

    plt.figure(figsize=(8, 6))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=colors, font_size=10, font_color='white', font_weight='bold', edge_color='gray')
    plt.title("Максимальна бінарна купа")
    plt.show()

heap_root = MaxHeapNode(90, color="lightblue")
heap_root.left = MaxHeapNode(80, color="lightblue")
heap_root.right = MaxHeapNode(85, color="lightblue")
heap_root.left.left = MaxHeapNode(70, color="lightblue")
heap_root.left.right = MaxHeapNode(50, color="lightblue")
heap_root.right.left = MaxHeapNode(75, color="lightblue")
heap_root.right.right = MaxHeapNode(60, color="lightblue")
heap_root.left.left.left = MaxHeapNode(40, color="lightblue")
heap_root.left.left.right = MaxHeapNode(45, color="lightblue")
heap_root.left.right.left = MaxHeapNode(55, color="lightblue")
heap_root.left.right.right = MaxHeapNode(65, color="lightblue")

draw_max_heap(heap_root)
