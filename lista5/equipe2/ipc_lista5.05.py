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

def examinar_permutacao(matriz,linha,coluna):
    for i in range(linha):
        acumulador_linha = 0
        acumulador_coluna = 0
        for j in range(coluna):
            if(matriz[i][j] == 0 or matriz[i][j] == 1):
                if(matriz[i][j] == 1):
                    acumulador_linha += 1
                if(matriz[j][i] == 1):
                    acumulador_coluna += 1
        if(acumulador_linha == 1 and acumulador_coluna == 1):
            return ("Matriz de permutacao!")
        else:
            return ("Nao e uma matriz de permutacao!")

linha = int(input("Quantidade de linhas:"))
coluna = int(input("Quantidade de colunas:"))
matriz = produzir_matriz(linha,coluna)
print(examinar_permutacao(matriz,linha,coluna))
