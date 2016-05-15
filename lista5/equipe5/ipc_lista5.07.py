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
            numero = int(input("linha %d,coluna %d:"%(i+1,j+1)))
            linha.append(numero)
        matriz.append(linha)
    return matriz

def mostrar_matriz(matriz,linha):
    print("matriz")
    for i in range(linha):
        print(matriz[i])

def somar_linha(matriz,linha,coluna,acms):
    acms = []
    for i in range(linha):
        acm = 0
        for j in range(coluna):
            acm += matriz[i][j]
        acms.append(acm)
    return (acms)

def somar_coluna(matriz,linha,coluna,acms):
    acms = []
    for i in range(linha):
        acm = 0
        for j in range(coluna):
            acm += matriz[j][i]
        acms.append(acm)
    return acms

def somar_diagonal(matriz,linha,coluna,acm,acm1):
    for i in range(linha):
        for j in range(coluna):
            if (i == j):
                acm += matriz[i][j]
            if ((i+j) == (linha-1)):
                acm1 += matriz[i][j]
    return acm, acm1

def verificar_cubo(lista):
    cont = 0
    for i in lista:
        if i == lista[0]:
            cont += 1
    if cont == len(lista):
        print ("e um cubo magico")
    else:
        print ("nao e um cubo magico")

acms1 = []
acms2 = []
acm1 = 0
acm2 = 0

linha = int(input("digite o valor para ser matriz quadrada: "))
coluna = linha
matriz = criar_matriz(linha,coluna)
mostrar_matriz(matriz,linha)
a = somar_linha(matriz,linha,coluna,acms1)
b = somar_coluna(matriz,linha,coluna,acms2)
c = somar_diagonal(matriz,linha,coluna,acm1,acm2)
a.extend(b)
a.extend(c)
verificar_cubo(a)
