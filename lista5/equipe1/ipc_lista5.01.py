#Introducao a programacao de computadores
#Professor: Jucimar Junior
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Nahan Trindade Passos - 1615310021


def criar_matriz(linha, coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            num = int(input("A(%d%d): \t"%(i+1, j+1)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def criar_vetor(coluna):
    vetor = []
    for i in range(coluna):
        num = int(input("V(%d): \t"%(i+1)))
        vetor.append(num)
    return vetor

def multiplicar(matriz, vetor):
    linha = len(matriz)
    coluna = len(matriz[0])
    resultado = []
    for i in range(linha):
        acm = 0
        for j in range(coluna):
            acm += matriz[i][j] * vetor[j]
        resultado.append(acm)
    return resultado

print ("Criar a matriz:")
linha = int(input("Quantas linhas tem sua matriz? "))
coluna = int(input("Quantas colunas tem sua matriz? "))
matriz = criar_matriz(linha, coluna)
print ("\nMatriz:")
for i in range(len(matriz)):
    print (matriz[i])

print ("\nCriar vetor:")
colunav = coluna
vetor = criar_vetor(colunav)
print ("\nVetor:\n",vetor)

produto = multiplicar(matriz, vetor)
print ("\nProduto de matriz por vetor =",produto)
