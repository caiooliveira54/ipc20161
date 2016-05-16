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
def examinar_matriz_nula(matriz,linha,coluna):
    acm_linha_nula = 0
    acm_coluna_nula = 0
    for i in range(linha):
        acm_linha = 0
        acm_coluna = 0
        for j in range(coluna):
            if(j < linha and i < linha):
                if(matriz[i][j] == 0):
                    acm_linha += 1
                    if(acm_linha == linha or acm_linha == coluna):
                        acm_linha_nula += 1
            if(j < linha and i < linha):
                if(matriz[j][i] == 0):
                    acm_coluna += 1
                    if(acm_coluna == linha or acm_coluna == coluna):
                        acm_coluna_nula += 1
    return("Quantidade de linhas nulas: %s,quantidade de colunas nulas: %s"%(acm_linha_nula,acm_coluna_nula))

linha = int(input("Quantidade de linhas:"))
coluna = int(input("Quantidade de colunas:"))
matriz = produzir_matriz(linha,coluna)
visualizar_matriz(matriz,linha)
print(examinar_matriz_nula(matriz,linha,coluna))
