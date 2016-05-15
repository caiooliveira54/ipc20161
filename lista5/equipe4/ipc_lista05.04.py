#Introdução a programação de computadores
#Professor: Jucimar Junior
#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Luiz Gustavo de Rocha Melo - 1615310015

def gerar_matriz(m, n):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            valor = int(input("Matriz %d%d: "%(i, j)))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def verificar_repetiçao(matriz):
    vetor = []
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            vetor.append(matriz[i][j])
    if len(vetor) == len(set(vetor)):
        print("Nao existem elementos repetidos")
    else:
        print("Existem elementos repetidos")

def mostrar_matriz(linhas):
    for i in range(linhas):
        print(matriz[i])

linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))
matriz = gerar_matriz(linhas, colunas)
mostrar_matriz(linhas)
verificar_repetiçao(matriz)
