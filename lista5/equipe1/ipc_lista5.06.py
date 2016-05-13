#Introducao a programacao de computadores
#Professor: Jucimar Junior


def criar_matriz(linha, coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            num = int(input("A(%d%d): \t"%(i+1, j+1)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def verificar_nulas(matriz, linha, coluna):
    linha_nula = 0
    coluna_nula = 0
    for i in range(linha):
        acm_linha_nula = 0
        acm_coluna_nula = 0
        for j in range(coluna):
            if matriz[i][j] == 0:
                acm_linha_nula += 1
            if matriz[j][i] == 0:
                acm_coluna_nula += 1
        if acm_linha_nula == len(matriz):
            linha_nula += 1
        if acm_coluna_nula == len(matriz):
            coluna_nula += 1
    print ("Linhas nulas =", linha_nula)
    print ("Colunas nulas =", coluna_nula)

def imprimir(matriz):
    for i in range(len(matriz)):
        print (matriz[i])

print ("Criar matriz:")
linha = int(input("Quantas linhas possui sua matriz? "))
coluna = int(input("Quantas colunas possui sua matriz? "))
matriz = criar_matriz(linha, coluna)
print ("\nMatriz:")
imprimir(matriz)
print ("\nResultado:")
verificar_nulas(matriz, linha, coluna)
