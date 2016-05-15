def fazermatriz (linha, coluna):
    matriz =[]
    for i in range (1, linha+1):
        linha = []
        for j in range (1, coluna+1):
            num = int(input("Digite a posicao %i%i da matriz: " %(i,j)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def verificar_nulas(matriz,linha,coluna):
    n_linha = 0
    n_coluna = 0
    for i in range(linha):
        acm1 = 0
        acm2 = 0
        for j in range(coluna):
            if matriz[i][j] == 0:
                acm1 += 1
            if matriz[j][i] == 0:
                acm2 += 1
        if acm1 == linha or acm1 == coluna:
            n_linha += 1
	if acm2 == linha or acm2 == coluna:       
            n_coluna += 1    
    return n_linha, n_coluna


def mostrarmatriz(matriz, linha):
    for i in range(linha):
        print (matriz[i])
	
linha = int(input("Digite a quantidade de linhas da matriz: "))
coluna = int(input("Digite a quantidade de colunas da matriz: "))
matriz = fazermatriz (linha,coluna)
print ("Matriz")
mostrarmatriz(matriz,linha)
l_nula, c_nula = verificar_nulas(matriz, linha, coluna)
print ("Quantidade de linhas nulas: ", l_nula)
print ("Quantidade de colunas nulas: ", c_nula)
