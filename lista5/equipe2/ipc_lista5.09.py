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

def lerMatriz(matriz, m, n):
    cont = 1
    if(matriz[0][0] == 0 and  matriz[0][1] == 0 or  matriz[1][0] == 0):
        matriz[0][0] = cont
        cont+=1
    for i in range(m):
        for j in range(n):            
            if(matriz[i][j] != -1 and matriz[i-1][j-1] != 0):
                matriz[i][j] = cont
                cont+=1

                    
    return matriz

def imprimir(matriz, m):
    for i in range(m):
        print(matriz[i])

linha = int(input("Quantidade de linhas na matriz: "))
coluna = int(input("Quantidade de colunas na matriz: "))
matriz = produzir_matriz(linha,coluna)
imprimir((lerMatriz(matriz,3,3)),3)

'''Monitor: Gabriel Alonso
Membros: Kid Mendes de Oliveira Neto
Eduardo Maia Freire
Igor Menezes Sales Vieira''' 
