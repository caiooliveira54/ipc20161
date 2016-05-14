#Introducao a programacao de computadores
#Professor: Jucimar Junior
#samuel silva de frança - 1615310049
#bruno de oliveira freire - 1615310030
#Felipe Henrique Bastos Costa - 1615310032
def criar_matriz(linha,coluna):
    matriz=[]
    for i in range(linha):
        matriz.append([])
        for j in range(coluna):
            numero=int(input("digite o numero a ser colocado na matriz:"))
            matriz[i].append(numero)
    return matriz

def multiplicar_matriz(matrizA,matrizB):
    linhaA=len(matrizA)
    colunaA=len(matrizA[0])
    linhaB=len(matrizB)
    resultado=[]
    for i in range(linhaA):
        linha=[]
        for j in range(colunaA):
            acm=0
            for k in range(linhaB):
                acm+=matrizA[j][k]*matrizB[k][j]
            linha.append(acm)
        resultado.append(linha)
    return resultado

def mostrar_matriz(linha,matriz):
    for i in range(linha):
        print matriz[i]

print ("crie a matrizA:")
linhaA=int(input("digite quantidade de linhas da matrizA:"))
colunaA=int(input("digite quantidade de colunas da matrizA:"))
matrizA=criar_matriz(linhaA,colunaA)
print("-----------------matrizA-----------------")
mostrar_matriz(linhaA,matrizA)
print "--------------------------------------------"


print ("crie a matrizB")
linhaB=int(input("digite quantidade de linhas da matrizB:"))
colunaB=int(input("digite quantidade de colunas da matrizB:"))
matrizB=criar_matriz(linhaB,colunaB)
print("-----------------matrizB-----------------")
mostrar_matriz(linhaB,matrizB)


print "--------------------------------------------"
resultado=multiplicar_matriz(matrizA,matrizB)
print "resultado da multiplicaçao:"
mostrar_matriz(linhaA,resultado)

    