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

def multiplicar_matrizes(matrizA, matrizB):
    linhaA = len(matrizA)
    colunaA = len(matrizA[0])
    linhaB = len(matrizB)
    colunaB = len(matrizB[0])
    matrizres =[]
    if(colunaA != linhaB):
        return False
    else:
        for i in range(colunaA):
            vetor = []
            for j in range(linhaB):
               x = matrizA[i][j]*matrizB[j][i]
               vetor.append(x)
            matrizres.append(vetor)
    return matrizres

linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))
print("\nMatriz A\n")
matrizA = gerar_matriz(linhas, colunas)
print("\nMatriz B\n")
matrizB = gerar_matriz(linhas, colunas)
produto = multiplicar_matrizes(matrizA, matrizB)
print("Matriz A: ", matrizA)
print("Matriz B: ", matrizB)
print("Produto: ", produto)
                

        
