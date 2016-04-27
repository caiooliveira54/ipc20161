#Thiago Santos Borges - 1615310023
#Antônio Rodrigues de Souza Neto - 1615310028
#Aberto

"""Dadas duas matrizes reais  Amxn e Bnxp, calcular o produto de A por B"""

def criar_matriz(n_linhas,n_colunas):
    matriz = []
    for i in range(1,n_linhas + 1):
        linha = []
        for j in range(1,n_colunas + 1):
            valor = float(input("Elemento %i%i: "%(i,j)))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def multiplicar_matrizes(matrizA,matrizB):
    matrizC = []
    linhasA = len(matrizA)
    colunasA = len(matrizA[0])
    linhasB = len(matrizB)
    colunasB = len(matrizB[0])
    acm = 0
    
    for i in range(linhasA):
        for j in range(colunasA):
            valor = 0
            for k in range(linhasB):   
                valor += matrizA[i][k] * matrizB[k][j]
            matrizC.append(valor)
    return matrizC

linhasA = int(input("Numero de linhas da matriz A: "))
colunaAlinhaB = int(input("Numero de colunas da matriz A e linhas matriz B: "))
linhasB = int(input("Numero de colunas da matriz B: "))
print("Matriz A")
A = criar_matriz(linhasA,colunaAlinhaB)
print("Matriz B")
B = criar_matriz(linhasB,colunaAlinhaB)
C = multiplicar_matrizes(A,B)
print("Matriz A * Matriz B -> ",C)
