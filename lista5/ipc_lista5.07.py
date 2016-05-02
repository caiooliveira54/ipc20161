# Ana Beatriz Faria Frota
# Mateus Mota de Souza
# Nahan Trindade Passos

def verificar_linhas(matriz, linha, coluna, acms):
    acms = []
    for i in range(linha):
        acm = 0
        for j in range(coluna):
            acm += matriz[i][j]
        acms.append(acm)
    return (acms)
def verificar_colunas(matriz, linha, coluna, acms):
    acms = []
    for i in range(linha):
        acm = 0
        for j in range(coluna):
            acm += matriz[j][i]
        acms.append(acm)
    return acms

def verificar_diagonais(matriz, linha, coluna, acm, acm1):
    for i in range(linha):
        for j in range(coluna):
            if (i == j):
                acm += matriz[i][j]
            if ((i+j) == (linha-1)):
                acm1 += matriz[i][j]
    return acm, acm1

def gerar_matriz(linha, coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            num = int(input("Posição A(%d%d): \t"%(i, j)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz, linha):
    for i in range(linha):
        print (matriz[i])

def verificar_cubo(lista):
    cont = 0
    for i in lista:
        if i == lista[0]:
            cont += 1
    if cont == len(lista):
        print ("É um cubo mágico")
    else:
        print ("Não é um cubo mágico")
        
acms1 = []
acms2 = []
acm1 = 0
acm2 = 0

linha = int(input("Qual a ordem da matriz? (A(nxn))\t"))
coluna = linha
print ("")
matriz = gerar_matriz(linha, coluna)
imprimir_matriz(matriz, linha)
a = verificar_linhas(matriz, linha, coluna, acms1)
b = verificar_colunas(matriz, linha, coluna, acms2)
c = verificar_diagonais(matriz, linha, coluna, acm1, acm2)
a.extend(b)
a.extend(c)
print ("")
verificar_cubo(a)
