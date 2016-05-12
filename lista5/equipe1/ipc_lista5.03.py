def criar_matriz(linha, coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            num = int(input("A(%d%d): \t"%(i+1, j+1)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def multiplicar(matriza, matrizb):
    resultado = []
    for i in range(len(matriza)):
        linha = []
        for j in range(len(matrizb[0])):
            acm = 0
            for l in range(len(matrizb)):
                acm += matriza[i][l] * matrizb[l][j]
            linha.append(acm)
        resultado.append(linha)
    return resultado

def imprimir(matriz):
    for i in range(len(matriz)):
        print (matriz[i])

print ("Criar Matriz A: ")
linha_a = int(input("Quantas linhas possui a matriz A? "))
coluna_a = int(input("Quantas colunas possui a matriz A? "))
matriza = criar_matriz(linha_a, coluna_a)
print ("\nMatriz A: ")
imprimir(matriza)

print ("\nCriar Matriz B: ")
linha_b = int(input("Quantas linhas possui a matriz B? "))
coluna_b = int(input("Quantas colunas possui a matriz B? "))
matrizb = criar_matriz(linha_b, coluna_b)
print ("\nMatriz B: ")
imprimir(matrizb)

print ("\nMatriz A * Matriz B =")
resultado = multiplicar(matriza, matrizb)
imprimir(resultado)
