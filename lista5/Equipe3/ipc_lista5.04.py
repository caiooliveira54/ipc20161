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


def verificar_repeticao(matriz):
    linha=len(matriz)
    coluna=len(matriz[0])
    acumulador = []
    for i in range(linha):
        for j in range(coluna):
            acumulador.append(matriz[i][j])
    if len(acumulador) == len(set(acumulador)):
        print "nao existe repeticao de elementos na matriz"
    else:
        print "existe alguma repetiçao de elementos na matriz"
def mostrar_matriz(linha,matriz):
    for i in range(linha):
        print matriz[i]

linha=int(input("digite o numero de linhas:"))
coluna=int(input("digite o numero de colunas"))
matrizA=criar_matriz(linha,coluna)
print "essa e a matriz="
mostrar_matriz(linha,matrizA)
verificar_repeticao(matrizA)
