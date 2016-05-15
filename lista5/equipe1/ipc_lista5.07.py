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

def verificar_cubo(matriz, linha, coluna):
    somas = []
    acm_diagonalp = 0
    acm_diagonals = 0
    for i in range(linha):
        acm_linha = 0
        acm_coluna = 0
        for j in range(coluna):
            acm_linha += matriz[i][j]
            acm_coluna += matriz[j][i]
            if i == j:
                acm_diagonalp += matriz[i][j]
            if i + j == (len(matriz) - 1):
                acm_diagonals += matriz[i][j]
        somas.append(acm_linha)
        somas.append(acm_coluna)
    somas.append(acm_diagonalp)
    somas.append(acm_diagonals)
    if len(set(somas)) == 1:
        print ("É um cubo mágico")
    else:
        print ("Não é um cubo mágico")

def imprimir(matriz):
    for i in range(len(matriz)):
        print (matriz[i])

print ("Criar Matriz: ")
linha = int(input("Quantas linhas possui a matriz? "))
coluna = int(input("Quantas colunas possui a matriz? "))
matriz = criar_matriz(linha, coluna)
print ("\nMatriz:")
imprimir(matriz)
print ("\nResultado:")
verificar_cubo(matriz, linha, coluna)
