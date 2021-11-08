'''
Algoritmo implementado em Python 3
Implementado por: Israel Santos Viera
Exercicio: Móbile (URI) https://www.beecrowd.com.br/judge/pt/problems/view/2323
'''

FECHADO = -1


def main(lista):
    balanceado = True

    for vertice in range(len(lista)):
        # Verifica se a quantidade de filhos do vértice atual é maior que zero
        if len(lista[vertice]) <= 0:
            continue

        sub_mobiles = 0
        # Percorre a lista de filhos do vértice atual para encontrar
        # um possível desbalanceamento, comparando o tamanho dos filhos
        # através de uma DFS
        for i in range(len(lista[vertice])):
            filho = lista[vertice][i]
            qtd_filhos = dfs(lista, filho)
            if i == 0:
                sub_mobiles = qtd_filhos

            if qtd_filhos != sub_mobiles:
                balanceado = False
                break

    if balanceado:
        print('bem')
    else:
        print('mal')


def dfs(lista, vertice):
    global filhos
    filhos = 0
    # Foi feita uma cópia da lista para não alterar os valores originais
    dfs_visitar(lista.copy(), vertice)
    return filhos


def dfs_visitar(lista, vertice):
    global filhos
    filhos += 1
    vizinhos = lista[vertice]

    for i in vizinhos:
        if i != FECHADO:
            dfs_visitar(lista, i)

    vertice = FECHADO


# Main -----
mobiles = int(input())
lista = [[] for i in range(mobiles+1)]

# Percorrendo a matriz para inserir os elementos por input
for vertice in range(mobiles):
    input_i, input_j = input().split(' ')
    i = int(input_i)
    j = int(input_j)
    lista[j].append(i)

main(lista)
