def criar_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            numero = int(input("linha %d,coluna %d:"%(i+1,j+1)))
            linha.append(numero)
        matriz.append(linha)
    return matriz

def verificar_repeticao(matriz):
    vetor = []
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            vetor.append(matriz[i][j])
    if len(vetor) == len(set(vetor)):
        print ("Não existem elementos repetidos")
    else:
        print ("Existem elementos repetidos")

def mostrar_matriz(matriz,linha):
    print("matriz")
    for i in range(linha):
        print(matriz[i])

linha = int(input("Quantas linhas tem sua matriz? "))
coluna = int(input("Quantas colunas tem sua matriz? "))
matriz = criar_matriz(linha,coluna)
mostrar_matriz(matriz,linha)
verificar_repeticao(matriz)
