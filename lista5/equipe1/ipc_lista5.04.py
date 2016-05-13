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

def verificar(matriz):
    vetor = []
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            vetor.append(matriz[i][j])

    if len(vetor) == len(set(vetor)):
        print ("Não existem elementos repetidos")
    else:
        print ("Existem elementos repetidos")

def imprimir(matriz):
    for i in range(len(matriz)):
        print (matriz[i])

print ("Criar a matriz:\n")
linha = int(input("Quantas linhas possuem a matriz? "))
coluna = int(input("Quantas colunas possuem a matriz? "))
matriz = criar_matriz(linha, coluna)
print ("\nMatriz: ")
imprimir(matriz)
print ("\nResultado:")
verificar(matriz)
