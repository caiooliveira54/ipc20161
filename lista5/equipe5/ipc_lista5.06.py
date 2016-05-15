def criar_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            numero = int(input("linha %d,coluna %d:"%(i+1, j+1)))
            linha.append(numero)
        matriz.append(linha)
    return matriz

def mostrar_matriz(matriz, linhas):
    print("matriz")
    for i in range(linhas):
        print(matriz[i])

def verificar_nulas (matriz,linha,coluna):
    ac_linha = 0
    ac_coluna = 0
    for i in range(linha):
        ac1 = 0
        ac2 = 0
        for j in range(coluna):
            if j < linha and i < coluna:
                if matriz[i][j] == 0:
                    ac1 += 1
                    if ac1 == linha or ac1 == coluna:
                        ac_linha += 1
            if j < linha and i < coluna:
                if matriz[j][i] == 0:
                    ac2 += 1
                    if ac2 == coluna or ac2 == linha:
                        ac_coluna += 1
    print("Numero de Linhas nulas %d, e numero de colunas nulas %d" %(ac_linha, ac_coluna))

m=int(input("Numero de linhas: "))
n=int(input("Numero de colunas: "))


matriz = criar_matriz(m,n)
mostrar_matriz(matriz,m)
verificar_nulas(matriz,m,n)
