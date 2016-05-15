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
def visualizar_matriz(matriz,linha):
    for i in range(linha):
        print(matriz[i])

def examinar_repeticao(matriz,linha,coluna):
    formar_matriz = []
    for i in range(linha):
        for j in range(coluna):
            formar_matriz.append(matriz[i][j])
    if(len(formar_matriz) == len(set(formar_matriz))):
        return ("Os elementos nao se repetem")
    else:
        return ("Existe elementos que se repetem na matriz")

linha = int(input("Quantidade de linhas:"))
coluna = int(input("Quantidade de colunass:"))
matriz = produzir_matriz(linha,coluna)
print(examinar_repeticao(matriz,linha,coluna))
