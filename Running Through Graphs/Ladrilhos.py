'''
Algoritmo implementado em Python 3
Implementado por: Israel Santos Viera
Exercicio: Ladrilhos (URI) https://www.beecrowd.com.br/judge/pt/problems/view/2246
'''

FECHADO = -1

def criar_matriz(linhas, colunas, valor_inicial):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(valor_inicial)
        matriz.append(linha)

    return matriz


def dfs(matriz, linhas, colunas):
    menor_grupo = 40001
    valido = True
    for i in range(linhas):
        if not valido:
            break

        for j in range(colunas):
            if matriz[i][j] != FECHADO:
                grupo = dfs_recursivo(matriz, i, j, linhas, colunas)
                if grupo == 1:
                    menor_grupo = 1
                    valido = False
                    break

                if menor_grupo > grupo:
                    menor_grupo = grupo

    print(menor_grupo)


def dfs_recursivo(matriz, i, j, qtd_linhas, qtd_colunas, grupo_atual=0):
    print(f'Posição {i}:{j}')
    if i < 0 or i >= qtd_linhas or j < 0 or j >= qtd_colunas:
        return

    grupo_atual += 1
    vertice_atual = matriz[i][j]
    matriz[i][j] = FECHADO

    cima = i-1
    baixo = i+1
    esquerda = j-1
    direita = j+1

    if cima >= 0:
        if matriz[cima][j] != FECHADO and matriz[cima][j] == vertice_atual:
            grupo_atual = dfs_recursivo(matriz, cima, j, qtd_linhas, qtd_colunas, grupo_atual)

    if baixo < qtd_linhas:
        if matriz[baixo][j] != FECHADO and matriz[baixo][j] == vertice_atual:
            grupo_atual = dfs_recursivo(matriz, baixo, j, qtd_linhas, qtd_colunas, grupo_atual)

    if esquerda >= 0:
        if matriz[i][esquerda] != FECHADO and matriz[i][esquerda] == vertice_atual:
            grupo_atual = dfs_recursivo(matriz, i, esquerda, qtd_linhas, qtd_colunas, grupo_atual)

    if direita < qtd_colunas:
        if matriz[i][direita] != FECHADO and matriz[i][direita] == vertice_atual:
            grupo_atual = dfs_recursivo(matriz, i, direita, qtd_linhas, qtd_colunas, grupo_atual)

    return grupo_atual


# Main -----
i_linhas, i_colunas = input().split(' ')
linhas = int(i_linhas)
colunas = int(i_colunas)

# Matriz que armazena as cores em cada posição
matriz = criar_matriz(linhas, colunas, 0)

# Percorrendo a matriz para inserir os elementos por input
for i in range(linhas):
    entrada = input().split(' ')
    for j in range(colunas):
        matriz[i][j] = int(entrada[j])

dfs(matriz, linhas, colunas)