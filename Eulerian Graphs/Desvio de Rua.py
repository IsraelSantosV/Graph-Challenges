'''
Algoritmo implementado em Python 3
Implementado por: Israel Santos Viera
Exercício: Desvio de Rua (URI) - 1442 https://www.beecrowd.com.br/judge/pt/problems/view/1442
'''

class Grafo:
    def __init__(self, lista_adj):
        self.lista_adj = lista_adj[:]
        
    def add_aresta(self, u, v, direcionado):
        self.lista_adj[u].append(v)
        
        if not direcionado:
            self.lista_adj[v].append(u)
            
    def eh_conexo(self):
        visitados = set()
    
        def dfs_iterativa(vertice_fonte):
            visitados.add(vertice_fonte)
            falta_visitar = [vertice_fonte]
            while falta_visitar:
                vertice = falta_visitar.pop()
                for vizinho in self.lista_adj[vertice]:
                    if vizinho not in visitados:
                        visitados.add(vizinho)
                        falta_visitar.append(vizinho)
    
        dfs_iterativa(0)
        return len(visitados) >= len(self.lista_adj)
    
    def pontes_recusivo(self, vertice_u):
        self.tempo += 1
        self.visitados[vertice_u] = True
        self.tempo_vertice[vertice_u] = self.tempo
        self.low_vertice[vertice_u] = self.tempo
        
        for v in self.lista_adj[vertice_u]:
            if self.visitados[v] == False:
                self.pai_vertice[v] = vertice_u
                self.pontes_recusivo(v)
                
                self.low_vertice[vertice_u] = min(self.low_vertice[vertice_u], self.low_vertice[v])
                
                if self.low_vertice[v] > self.tempo_vertice[vertice_u]:
                    self.bridges.append((vertice_u, v))
            
            elif v != self.pai_vertice[vertice_u]:
                self.low_vertice[vertice_u] = min(self.low_vertice[vertice_u], self.tempo_vertice[v])
            
    def encontrar_pontes(self):
        tamanho = len(self.lista_adj)
        self.tempo = 0
        self.visitados = [False] * tamanho
        self.tempo_vertice = [float("Inf")] * tamanho
        self.low_vertice = [float("Inf")] * tamanho
        self.pai_vertice = [-1] * tamanho
        
        self.bridges = []
        
        for i in range(tamanho):
            if self.visitados[i] == False:
                self.pontes_recusivo(i)
                
        return self.bridges

''' Lógica:
Cria dois grafos, um direcionado e outro não direcionado para representar o grafo inicial
Obs: A rua inicial é retirada antes da execução do algoritmo

- Pegar o grafo não direcionado e verificar se é conexo:
    se não for = '*',
    caso seja:
        se o direcionado também é conexo = '-'.

- Procuro por alguma ponte no grafo unidirecional:
    caso encontre alguma = '2', 
    senão = '1'.
'''


while True:
    try:
        N,M = input().split(' ')
        lista_adj = [[] for i in range(int(N))]
        G_direcionado = Grafo(lista_adj)
        G_nao_direcionado = Grafo(lista_adj)
        
        for i in range(int(M)):
            A,B,T = input().split(' ')
            if i != 0:
                G_direcionado.add_aresta((int(A)-1), (int(B)-1), int(T) == 1)
                G_nao_direcionado.add_aresta((int(A)-1), (int(B)-1), False)
            
        if not G_nao_direcionado.eh_conexo():
            print('*')
        elif G_direcionado.eh_conexo():
            print('-')
        else:
            pontes_dir = G_direcionado.encontrar_pontes()
            if len(pontes_dir) > 0:
                pontes_nao_dir = G_nao_direcionado.encontrar_pontes()
                for p_1 in pontes_dir:
                    inverso = (p_1(1), p_1(0))
                    for p_2 in pontes_nao_dir:
                        if p_2 == inverso:
                            print('2')
                            break
            else:
                print('1')
    except EOFError:
        break