#Introducao a programacao de computadores
#Professor: Jucimar Junior
#samuel silva de frança - 1615310049
#bruno de oliveira freire - 1615310030
#Felipe Henrique Bastos Costa - 1615310032
#Monitor: Delrick Oliveira

def multiplicar_vetor(matriz,vetor):
    matriz_multi = []
    for i in range(len(matriz)):
        acm = 0
        for j in range(len(matriz[0])):
            acm += matriz[i][j]*vetor[j]
        matriz_multi.append(acm)
    return matriz_multi

def criar_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        listainterna = []
        for j in range(colunas):
            num = int(input("A(%d%d): "%(i+1,j+1)))
            listainterna.append(num)
        matriz.append(listainterna)
    return matriz

def criar_vetor(colunas):
    vetor = []
    for i in range(colunas):
        num = int(input("Informe o valor do A%d: "%(i+1)))
        vetor.append(num)
    return vetor

def verificar_resultado(matriz,matriz2):
    if matriz == matriz2:
        return "A matriz e a solucao"
    else:
        return "A matriz nao e a solucao"

linhas = int(input("Informe o numero de linhas da matriz: "))
colunas = int(input("Informe o numero de colunas da matriz: "))
matriz = criar_matriz(linhas,colunas)
vetor = criar_vetor(colunas)

colunas_solucao = int(input("Informe quantos elementos tem a solucao: "))
solucao = criar_vetor(colunas_solucao)

matriz_multi = multiplicar_vetor(matriz,vetor)
print verificar_resultado(matriz_multi,solucao)
