def criar_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            numero = int(input("linha %d,coluna %d:"%(i+1,j+1)))
            linha.append(numero)
        matriz.append(linha)
    return matriz

def mostrar_matriz(matriz,linhas):
    print("matriz")
    for i in range(linhas):
        print(matriz[i])

def verificar_permutacao (matriz,linha,coluna):
    for i in range (linha):
        ac = 0
        ac2 = 0
        for j in range(coluna):
            if matriz[i][j] == 0 or matriz[i][j]== 1: 
                if matriz[i][j] == 1:
                    ac += 1
                if matriz[j][i] == 1:
                    ac2 += 1
            else:
                return("Nao e de permutacao")
        if (ac == 1 and ac2 == 1):
            return("E de permutacao")
        else:
            return("Nao e permutacao")

linha = int(input("quantidade de linhas: " ))
coluna = int(input("quantidade de colunas: "))
matriz = criar_matriz(linha,coluna)
mostrar_matriz(matriz, linha)
resultado = verificar_permutacao(matriz,linha,coluna)
print(resultado)
