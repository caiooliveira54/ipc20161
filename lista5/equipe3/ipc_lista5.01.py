#Introducao a programacao de computadores
#Professor: Jucimar Junior
#samuel silva de frança - 1615310049
#bruno de oliveira freire - 1615310030
#Felipe Henrique Bastos Costa - 1615310032
def gerar_matriz(m,n):
    matriz = []
    for i in range(1,m+1):
        linhas = []
        for j in range(1,n+1):
            num = int(input("A%d%d : " %(i+1 , j+1)))
            linhas.append(num)
        matriz.append(linhas)
    return matriz

def gerar_vetor(n):
    vetor = []
    for i in range(n):
        num = int(input("V%d : " % (i)))
        vetor.append(num)
    return vetor

def multiplicar_matriz_vetor(matriz,vetor):
    multi = []
    for i in range(len(matriz)):
        acm = 0
        for j in range(len(vetor)):
            acm = acm + matriz[i][j]*vetor[j]
        multi.append(acm)
    return multi

linhas = int(input())
colunas = int(input())
matriz = gerar_matriz(linhas,colunas)
vetor = gerar_vetor(colunas)
produto = multiplicar_matriz_vetor(matriz,vetor)
print(produto)
    
