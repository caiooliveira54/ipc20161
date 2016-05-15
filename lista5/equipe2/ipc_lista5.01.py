#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Kid Mendes de Oliveira Neto - 1615310011
#Eduardo Maia Freire - 1615310003
#Igor Menezes Sales Vieira - 1615310007
#

def produzir_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            numero = int(input("A(%s%s): "%(i,j)))
            linha.append(numero)
        matriz.append(linha)
    return matriz

def produzir_vetor(coluna):
    vetor = []
    for i in range(coluna):
        numero = int(input("V(%s): "%i))
        vetor.append(numero)
    return vetor
def produto_matriz_vetor(matriz,vetor,linha,coluna):
    produto = []
    for i in range(linha):
        acumulador = 0
        for j in range(coluna):
            acumulador += matriz[i][j] * vetor[j]
        produto.append(acumulador)
    return produto

linha = int(input("Quantidade de linhas na matriz: "))
coluna = int(input("Quantidade de colunas na matriz: "))
matriz = produzir_matriz(linha,coluna)
vetor = produzir_vetor(coluna)
produto = produto_matriz_vetor(matriz,vetor,linha,coluna)
print("O produto da matriz pelo vetor sera: %s"%(produto))
