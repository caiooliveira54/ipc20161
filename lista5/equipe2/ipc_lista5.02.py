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

def produzir_vetor(coluna):
    vetor = []
    for i in range(coluna):
        numero = int(input("V(%s): "%i))
        vetor.append(numero)
    return vetor
def produto_matriz_vetor(matriz,vetor,linha,coluna):
    produto = []
    for i in range(linha):
        acumulador = 0
        for j in range(coluna):
            acumulador += matriz[i][j] * vetor[j]
        produto.append(acumulador)
    return produto
def examinar_resultado(usuario_vetor,produto):
    if(usuario_vetor != produto):
        return ("O resultado nao sera compativel com o valor informado pelo usuario")
    else:
        return("O resultado sera compativel com o valor informado pelo usuario")

#Previsao do usuario
usuario_tamanho_vetor = int(input("Tamanho do vetor resultado:"))
usuario_vetor = produzir_vetor(usuario_tamanho_vetor)
#Criar Matriz
linha = int(input("Quantidade de linhas na matriz: "))
coluna = int(input("Quantidade de colunas na matriz: "))
matriz = produzir_matriz(linha,coluna)
#Criar Vetor
vetor = produzir_vetor(coluna)
#Produto da Matriz pelo Vetor
produto = produto_matriz_vetor(matriz,vetor,linha,coluna)
print("O produto da matriz pelo vetor sera: %s"%(produto))
#Verificar a previsao do usuario
print(examinar_resultado(usuario_vetor,produto))
