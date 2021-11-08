'''
Algoritmo implementado em Python 3
Implementado por: Israel Santos Viera
Exercício: Mania de Par (URI) - 1931 https://www.beecrowd.com.br/judge/pt/problems/view/1931
'''

import heapq
INF = 10000000
INDEX = 0
WEIGHT = 1

class Graph:
    def __init__(self, vertex_size):
        self.vertex_size = vertex_size
        self.graph = [[] for i in range(vertex_size)]

    def add_edge(self, u, v, weight):
        self.graph[u].append([v, weight])

    def dijkstra(self, origin, destination):
        distances = [INF for i in range(self.vertex_size)]
        visitors = [False for i in range(self.vertex_size)]

        myHeap = [[origin, distances[origin]]]
        heapq.heapify(myHeap)

        distances[origin] = 0

        while len(myHeap) > 0:
            currentElement = heapq.heappop(myHeap)
            u = currentElement[INDEX]

            if not visitors[u]:
                visitors[u] = True

                for neighbor in self.graph[u]:
                    v = neighbor[INDEX]
                    weight = neighbor[WEIGHT]

                    if distances[v] > (distances[u] + weight):
                        distances[v] = distances[u] + weight
                        heapq.heappush(myHeap, [v, distances[v]])

        return distances[destination]

# Main
C_input,V_input = input().split(' ')
C = int(C_input)
V = int(V_input)

G = Graph(C)
G_aux = Graph(C)

for i in range(V):
    u,v,weight = input().split(' ')
    G.add_edge(int(u)-1, int(v)-1, int(weight))

# Criar um grafo auxiliar para satisfazer a condição necessária (análogo à ordenação topológica em grafo acíclicos)
for i in range(C):
    for neighbor in G.graph[i]:
        index = neighbor[INDEX]
        weight = neighbor[WEIGHT]
        neighbor_size = len(G.graph[index])

        if neighbor_size > 0:
            for neighbor_neighbor in G.graph[index]:
                neighbor_index = neighbor_neighbor[INDEX]
                neighbor_weight = neighbor_neighbor[WEIGHT]
                G_aux.add_edge(i, neighbor_index, weight + neighbor_weight)

min_pass = G_aux.dijkstra(0, C-1)

if min_pass == INF:
    print(-1)
else:
    print(min_pass)