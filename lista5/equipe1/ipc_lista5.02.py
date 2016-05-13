#Introducao a programacao de computadores
#Professor: Jucimar Junior
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza
# Nahan Trindade Passos - 1615310021

def criar_matriz(linha, coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            num = int(input("A(%d%d): \t"%(i+1, j+1)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def criar_vetor(coluna):
    vetor = []
    for i in range(coluna):
        num = int(input("V(%d): \t"%(i+1)))
        vetor.append(num)
    return vetor

def multiplicar(matriz, vetor):
    linha = len(matriz)
    coluna = len(matriz[0])
    resultado = []
    for i in range(linha):
        acm = 0
        for j in range(coluna):
            acm += matriz[i][j] * vetor[j]
        resultado.append(acm)
    return resultado

def verificar(vetor, resultado):
    if vetor == resultado:
        print ("Os valores informados são resultados")
    else:
        print ("Os valores informados não são resultados")

print ("Criar vetor com resultados a serem verificados")
l_resultado = int(input("\nQuantos elementos possuem o vetor resultado? "))
soluçao = criar_vetor(l_resultado)
print ("Possivel Soluçao =", soluçao)

print ("\nCriar matriz A")
linha = int(input("Quantas linhas possuem sua matriz? "))
coluna = int(input("Quantas colunas possuem sua matriz? "))
matriz = criar_matriz(linha, coluna)
print ("\nMatriz A:")
for i in range(len(matriz)):
    print (matriz[i])
    
print ("\nCriar vetor X")
colunav = coluna
vetor = criar_vetor(colunav)
print ("\nVetor X =", vetor)

resultado = multiplicar(matriz, vetor)
print ("\nResultado da multiplicação =", resultado, "\n")
verificar(soluçao, resultado)
