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

def verificar_permutaçao(matriz, linha, coluna):
    permutaçao = 0
    for i in range(linha):
        acm_um_linha = 0
        acm_um_coluna = 0
        acm_zero_linha = 0
        acm_zero_coluna = 0
        for j in range(coluna):
            if matriz[i][j] == 0:
                acm_zero_linha += 1
            if matriz[i][j] == 1:
                acm_um_linha += 1
            if matriz[j][i] == 0:
                acm_zero_coluna += 1
            if matriz[j][i] == 1:
                acm_um_coluna += 1
        if (acm_um_linha == acm_um_coluna == 1) and (acm_zero_linha == acm_zero_coluna == (len(matriz)-1)):
            permutaçao += 1
    if permutaçao == len(matriz):
        print ("É de permutação")
    else:
        print ("Não é de permutação")

def imprimir(matriz):
    for i in range(len(matriz)):
        print (matriz[i])
        
print ("Criar Matriz:")
linha = int(input("Quantas linhas possui a matriz? "))
coluna = int(input("Quantas colunas possui a matriz? "))
matriz = criar_matriz(linha, coluna)
print ("\nMatriz:")
imprimir(matriz)
print ("\nResultado:")
verificar_permutaçao(matriz, linha, coluna)
