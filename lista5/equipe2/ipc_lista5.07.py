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
def examinar_matriz_quadrada(matriz,linha,coluna):
    acm_quadrado_magico = []
    acm_diagonal_principal = 0
    acm_diagonal_secundaria = 0
    cont = 0
    for i in range(linha):
        acm_linha = 0
        for j in range(coluna):
            acm_linha += matriz[i][j]
        acm_quadrado_magico.append(acm_linha)
    for i in range(linha):
        acm_coluna = 0
        for j in range(coluna):
            acm_coluna += matriz[j][i]
        acm_quadrado_magico.append(acm_coluna)
    for i in range(linha):
        for j in range(coluna):
            if(i == j):
                acm_diagonal_principal += matriz[i][j]
            if((i+j) == (coluna -1)):
                acm_diagonal_secundaria += matriz[i][j]
    acm_quadrado_magico.append(acm_diagonal_principal)
    acm_quadrado_magico.append(acm_diagonal_secundaria)
    return acm_quadrado_magico

def examinar_cubo(cubo):
    if(len(set(cubo)) == 1):
        return ("Cubo magico!")
    else:
        return ("Nao e um cubo magico")

linha = int(input("Quantidade de linhas da matriz quadrada:"))
coluna  = linha
matriz= produzir_matriz(linha,coluna)
cubo = examinar_matriz_quadrada(matriz,linha,coluna)
print(examinar_cubo(cubo))
 
