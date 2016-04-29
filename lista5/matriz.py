def gerar_matriz(m, n):
    matriz = []
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            num = int(input("A(%d%d):\t"%(i, j)))
            linha.append(num)
        matriz.append(linha)
    return matriz


def gerar_vetor(n):
    vetor = []
    for i in range(n):
        num = int(input("V(%d): \t"%(i)))
        vetor.append(num)
    return vetor


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
