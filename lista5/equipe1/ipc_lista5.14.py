def criar_matriz(linha, coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            num = int(input("Custo da cidade %d para a %d: \t"%(i+1, j+1)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def calcular_intinerario(matriz):
    vetor = []
    acm = 0
    intinerario = str(input("\nQual o intinerario? \t"))
    for a in range(len(intinerario)):
        vetor.append(int(intinerario[a]))
    for i in range(len(vetor)):
        if i == (len(vetor) - 1):
            break
        else:
            a = vetor[i]
            b = vetor[i+1]
            acm += matriz[a][b]
    return acm

def imprimir_matriz(matriz, linha):
    for i in range(linha):
        print (matriz[i])

linha = int(input("Qual a ordem da matriz com os valores das cidades? \t"))
coluna = linha
matriz = criar_matriz(linha, coluna)
print ("\nPreços das rotas:\n")
imprimir_matriz(matriz, linha)
calculo = calcular_intinerario(matriz)
print ("\nO valor do intinerario é R$%d"%(calculo))
