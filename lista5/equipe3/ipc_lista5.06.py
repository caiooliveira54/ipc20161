#Introducao a programacao de computadores
#Professor: Jucimar Junior
#samuel silva de frança - 1615310049
#bruno de oliveira freire - 1615310030
#Felipe Henrique Bastos Costa - 1615310032

def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            num = int(input("A(%d%d): "%(i+1, j+1)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def verificar_nulas(matriz,linhas,colunas):
    nula1 = 0
    nula2 = 0     
    for i in range(linhas):
        cont1 = 0
        cont2 = 0       
        for j in range(colunas):
            if matriz[i][j] == 0:
                cont1 += 1
            if matriz[j][i] == 0:
                cont2 += 1
        if cont1 == linhas:
            nula1 += 1
        if cont2 == colunas:
            nula2 += 1
    return("Numero de linhas nulas: %d\nNumero de colunas nulas: %d"%(nula1,nula2))

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print matriz[i]    

linhas = int(input("Informe o numero de linhas da matriz: "))
colunas = int(input("Informe o numero de colunas da matriz: "))
matrizA = criar_matriz(linhas,colunas)
mostrar_matriz(matrizA)

print verificar_nulas(matrizA,linhas,colunas)