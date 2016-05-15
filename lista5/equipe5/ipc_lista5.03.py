#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 5
#
#Ariel Guilherme Rocha Capistrano - 1615310029
#

def criar_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            numero = int(input("linha %d,coluna %d:"%(i+1, j+1)))
            linha.append(numero)
        matriz.append(linha)
    return matriz

def mostrar_matriz(matriz, linhas):
    print("matriz")
    for i in range(linhas):
        print(matriz[i])

def multiplicar_matriz(matriz_a,matriz_b):
    linha_a=len(matriz_a)
    coluna_a=len(matriz_a[0])
    linha_b=len(matriz_b)
    coluna_b=len(matriz_b[0])
    resultado=[]
    for i in range(linha_a):
        linha=[]
        for j in range(coluna_b):
            acm=0
            for k in range(linha_b):
                acm += matriz_a[i][k]*matriz_b[k][j]
            linha.append(acm)
        resultado.append(linha)
    return resultado

m = (int(input("digite a quantidade de linhas da primeira matriz: ")))
n = (int(input("digite a quantidade de linhas da primeira matriz e de colunas para a segunda: ")))
p = (int(input("digite a quantidade de colunas da segunda matriz: ")))
matriz_a = criar_matriz(m,n)
matriz_b = criar_matriz(n,p)
matriz_c = multiplicar_matriz(matriz_a,matriz_b)
mostrar_matriz(matriz_a,m)
mostrar_matriz(matriz_b,m)
mostrar_matriz(matriz_c,m)
