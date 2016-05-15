#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Kid Mendes de Oliveira Neto - 1615310011
#Eduardo Maia Freire - 1615310003
#Igor Menezes Sales Vieira - 1615310007
#

def produzir_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            numero = int(input("A(%s%s): "%(i,j)))
            linha.append(numero)
        matriz.append(linha)
    return matriz
def produto_matriz(matriz1,matriz2):
    produto = []
    for i in range(len(matriz1)):
        produto_linha = []
        for j in range(len(matriz2[0])):
            acumulador_produto = 0
            for k in range(len(matriz2)):
                acumulador_produto += matriz1[i][k] * matriz2[k][j]
            produto_linha.append(acumulador_produto)
        produto.append(produto_linha)
    return produto
def visualizar_matriz(matriz,linha):
    for i in range(linha):
        print(matriz[i])
def examinar_produto(coluna1,linha1,linha2,coluna2):
    if(coluna1 != linha2):
        return ("Nao sera possivel realizar o produto dessas matrizes")
    else:
        print("Matriz A")
        matriz1 = produzir_matriz(linha1,coluna1)
        print("Matriz B")
        matriz2 = produzir_matriz(linha2,coluna2)
        produto_matrizes = produto_matriz(matriz1,matriz2)
        mostrar_matriz1 = visualizar_matriz(matriz1,linha1)
        mostrar_matriz2 = visualizar_matriz(matriz2,linha2)
        mostrar_produto_matrizes = visualizar_matriz(produto_matrizes,linha1)
        return mostrar_matriz1,mostrar_matriz2,mostrar_produto_matrizes

print("Matriz A")
linha1 = int(input("Quantidade de linhas:"))
coluna1 = int(input("Quantidade de colunas:"))
print("Matriz B")
linha2 = int(input("Quantidade de linhas:"))
coluna2 = int(input("Quantidade de colunas:"))
examinar_produto(coluna1,linha1,linha2,coluna2)
