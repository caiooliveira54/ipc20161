#Introdução a programação de computadores
#Professor: Jucimar Junior
#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Luiz Gustavo de Rocha Melo - 1615310015

def gerar_matriz(m, n):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            valor = int(input("Matriz %d%d: "%(i, j)))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def gerar_vetor(n):
    vetor = []
    for i in range(n):
        valor = int(input("Vetor %d: "%i))
        vetor.append(valor)
    return vetor

def gerar_produto(matriz, vetor):
    linhas = len(matriz)
    colunas = len(matriz[0])
    produto = []
    for i in range(linhas):
        acm = 0
        for j in range(colunas):
            acm += matriz[i][j] * vetor[j]
        produto.append(acm)
    return produto

linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))
matriz = gerar_matriz(linhas, colunas)
print("Matriz: ")
for i in range(linhas):
    print(matriz[i])

vetor = gerar_vetor(colunas)
print(vetor)

produto = gerar_produto(matriz, vetor)
print(produto)
