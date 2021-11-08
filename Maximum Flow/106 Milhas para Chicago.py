'''
Algoritmo implementado em Python 3
Implementado por: Israel Santos Viera
Exercício: 106 Milhas para Chicago (URI) - 1655 https://www.beecrowd.com.br/judge/pt/problems/view/1655
'''

from collections import defaultdict
from heapq import *

class Graph:
    def __init__(self, size):
        self.edges = []
        self.ROW = size

    # Adicionando arestas para um grafo não direcionado com peso entre 0 e 1
    def add_edge(self, u, v, weight):
        self.edges.append((u,v,weight * 0.01))

    # Utilizei Dijkstra pela facilidade de implementação e pelos valores de pesos serem limitados a 100
    def dijkstra(self, source, destination):
        g = defaultdict(set)
        for u, v, cost in self.edges:
            g[u].add((cost, v))
            g[v].add((cost, u))

        # 'dist' registra o valor mínimo de cada nó na heap
        queue, seen, dist = [(1, source, ())], set(), {source: 0}
        heapify(queue)
        while queue:
            (cost, v1, path) = heappop(queue)
            if cost < 0:
                cost = cost * -1

            if v1 in seen: continue

            seen.add(v1)
            # path += (v1,)
            if v1 == destination:
                return cost

            max_child_flow = 0;
            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue

                # Nem toda aresta será calculada. A borda que pode melhorar o valor do nó no heap será útil.
                # Foi feita uma pequena alteração no algoritmo para multiplicar o custo pelo dist ao invés de somar
                if v2 not in dist or cost * c > dist[v2]:
                    dist[v2] = cost * c
                    heappush(queue, (-1 * (cost * c), v2, path)) # Usando Max Heap para pegar o maior valor

        return float("inf")

# Main
while True:
    allInput = input().split(' ')
    if allInput[0] == '0':
        break

    vertex = int(allInput[0])
    edges = int(allInput[1])

    # Create a graph
    G = Graph(vertex)

    S = 1
    T = vertex

    # Add edges into all graphs
    for i in range(edges):
        u,v,w = input().split(' ')
        G.add_edge(int(u), int(v), float(w))

    # Execute algorithm
    print('%.6f percent' % (G.dijkstra(S, T) * 100))