#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 5
#
#Ariel Guilherme Rocha Capistrano - 1615310029
#

def criar_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            numero = int(input("linha %d,coluna %d:"%(i+1, j+1)))
            linha.append(numero)
        matriz.append(linha)
    return matriz

def criar_vetor(coluna):
    vetor = []
    for i in range(coluna):
        numero = int(input("Vetor coluna %d:"%(i+1)))
        vetor.append(numero)
    print("vetor")
    print(vetor)
    return vetor

def mostrar_matriz(matriz, linhas):
    print("matriz")
    for i in range(linhas):
        print(matriz[i])

def multiplicar_linhavetor(matriz,vetor):
    linha = len(matriz)
    coluna = len(matriz[0])
    resultado = []
    for i in range(linha):
        acm = 0
        for j in range(coluna):
            acm += matriz[i][j] * vetor[j]
        resultado.append(acm)
    print("multiplicando")
    print(resultado)

linha = int(input("Quantas linhas tem sua matriz? "))
coluna = int(input("Quantas colunas tem sua matriz? "))
matriz = criar_matriz(linha,coluna)
vetor = criar_vetor(coluna)
mostrar_matriz(matriz, linha)
multiplicar_linhavetor(matriz,vetor)
