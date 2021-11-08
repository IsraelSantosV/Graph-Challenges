'''
Algoritmo implementado em Python 3
Implementado por: Israel Santos Viera
Exercício: Estradas Escuras (URI) - 1152 https://www.beecrowd.com.br/judge/pt/problems/view/1152
'''

from heapq import heappush, heappop, heapify

INFINITO = 2147483649
RAIZ = 0


class Vertice:
    def __init__(self, index):
        self.index = index
        self.chave = INFINITO
        self.pai = -1
        self.visitado = False


def get_peso(lista_pai, index):
    for i in range(len(lista_pai)):
        if lista_pai[i][0] == index:
            return lista_pai[i]


def prim(lista_adj, vertices, raiz):
    AGM = []
    heap = []

    vertices[raiz].chave = 0
    vertices[raiz].pai = raiz

    for i in range(len(vertices)):
        heap.append((vertices[i].chave, vertices[i].index))

    heapify(heap)

    while(len(heap) > 0):
        minimo = heappop(heap)[1]
        vertices[minimo].visitado = True

        for vizinho in lista_adj[minimo]:
            if(not vertices[vizinho[0]].visitado and vizinho[1] < vertices[vizinho[0]].chave):
                vertices[vizinho[0]].pai = minimo
                vertices[vizinho[0]].chave = vizinho[1]
                heappush(heap, (vertices[vizinho[0]].chave, vertices[vizinho[0]].index))

    for v in vertices:
        if(v.pai != v.index):
            peso = get_peso(lista_adj[v.pai], v.index)[1]
            AGM.append((v.pai, v, peso))

    return AGM


def calcular_valor(AGM):
    valor = 0
    for v in AGM:
        valor += v[2]

    return valor


while(True):
    i_vertices, i_arestas = input().split(' ')
    vertices = int(i_vertices)
    arestas = int(i_arestas)

    if vertices == 0 and arestas == 0:
        break

    lista_adj = [[] for i in range(vertices)]
    lista_vertices = []

    for i in range(vertices):
        lista_vertices.append(Vertice(i))

    valor_total = 0

    for i in range(arestas):
        i_x, i_y, valor = input().split(' ')
        lista_adj[int(i_x)].append((int(i_y), int(valor)))
        lista_adj[int(i_y)].append((int(i_x), int(valor)))
        valor_total += int(valor)

    AGM = prim(lista_adj, lista_vertices, RAIZ)
    print(valor_total - calcular_valor(AGM))