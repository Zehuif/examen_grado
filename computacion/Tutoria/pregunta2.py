#importar librería grafos
import random as r, networkx as nx

#crear grafo
g = nx.Graph()

#crear nodos
g.add_node("Arquitectura Software")
g.add_node("Ingeniería de Software y BD")
g.add_node("Sistemas Operativos")
g.add_node("Estructuras de Datos y Algoritmos")

#crear aristas entre todos los nodos con todos
g.add_edge("Arquitectura Software", "Ingeniería de Software y BD", weight = r.randint(1, 10))
g.add_edge("Arquitectura Software", "Sistemas Operativos", weight = r.randint(1, 10))
g.add_edge("Arquitectura Software", "Estructuras de Datos y Algoritmos", weight = r.randint(1, 10))
g.add_edge("Ingeniería de Software y BD", "Sistemas Operativos", weight = r.randint(1, 10))
g.add_edge("Ingeniería de Software y BD", "Estructuras de Datos y Algoritmos", weight = r.randint(1, 10))
g.add_edge("Sistemas Operativos", "Estructuras de Datos y Algoritmos", weight = r.randint(1, 10))

#imprimir grafo
print(g)

#imprimir nodos
print("Nodos: ", g.nodes())

#imprimir aristas
for edge in g.edges():
    print(edge)

#implementar algoritmo de prim
T = nx.minimum_spanning_tree(g, algorithm='prim')
print(T.edges(data=True))