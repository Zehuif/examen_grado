import networkx as nx
from networkx.algorithms import tree

# Crear el grafo
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2, weight=0.5)
G.add_edge(2, 3, weight=1.0)
G.add_edge(1, 3, weight=0.8)

# Implementar el algoritmo de Prim
T = nx.minimum_spanning_tree(G)

# Mostrar el árbol resultante
print(T.edges())

######kruskal
G = nx.cycle_graph(4)
G.add_edge(0, 3, weight=2)
mst = tree.minimum_spanning_edges(G, algorithm="kruskal", data=False)
edgelist = list(mst)
sorted(sorted(e) for e in edgelist)
print(edgelist)


######Prim
G = nx.cycle_graph(4)
G.add_edge(0, 3, weight=2)
mst = tree.minimum_spanning_edges(G, algorithm="prim", data=False)
edgelist = list(mst)
sorted(sorted(e) for e in edgelist)
print(edgelist)

