def gerar_matriz( m, n):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(1, n+1):
            num = int(input("A(%d%d):\t"%(i, j)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def gerar_matriz_vazia(m, n):
    matriz = []
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            num = 0
            linha.append(num)
        matriz.append(linha)
    return matriz
    
def verificar_permutacao (matriz, linha, coluna):
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
                return ("Nao e de permutacao")
        if (ac == 1 and ac2 == 1):
            return ("E de permutacao")
        else:
            return("Nao e permutacao")

def verificar_nulas (matriz,linha, coluna):
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
    return ("Numero de Linhas nulas %d, e numero de colunas nulas %d" %(ac_linha, ac_coluna))

def mostrar_matriz(matriz, linhas):
	for i in range(linhas):
		print(matriz[i])


def gerar_vetor(n):
    vetor = []
    for i in range(n):
        num = int(input("V(%d): \t"%(i)))
        vetor.append(num)
    return vetor


def multiplicar_matrizes(matrizA,matrizB):
    matrizC = []
    linhasA = len(matrizA)
    colunasA = len(matrizA[0])
    linhasB = len(matrizB)
    colunasB = len(matrizB[0])
    
    for i in range(linhasA):
        linhac = []
        for j in range(colunasB):
            acm = 0
            for k in range(linhasB):   
                acm += matrizA[i][k] * matrizB[k][j]
            linhac.append(acm)
        matrizC.append(linhac)
    return matrizC

def verificar_repeticao(matriz, linhas, colunas):
    lista = []
    for i in range(linhas):
        for j in range(colunas):
            lista.append(matriz[i][j])
    if len(lista) == len(set(lista)):
        return "Nao existem elementos repetidos na matriz"
    else:
        return "Existem elementos repetidos na matriz"

def verificar_linhas(matriz, linha, coluna, acms):
    acms = []
    for i in range(linha):
        acm = 0
        for j in range(coluna):
            acm += matriz[i][j]
        acms.append(acm)
    return (acms)

def verificar_colunas(matriz, linha, coluna, acms):
    acms = []
    for i in range(linha):
        acm = 0
        for j in range(coluna):
            acm += matriz[j][i]
        acms.append(acm)
    return acms

def verificar_diagonais(matriz, linha, coluna, acm, acm1):
    for i in range(linha):
        for j in range(coluna):
            if (i == j):
                acm += matriz[i][j]
            if ((i+j) == (linha-1)):
                acm1 += matriz[i][j]
    return acm, acm1
    
def verificar_cubo(lista):
    cont = 0
    for i in lista:
        if i == lista[0]:
            cont += 1
    if cont == len(lista):
        print ("É um cubo mágico")
    else:
        print ("Não é um cubo mágico")
        
def verificar(matriz, R):
    if R != B:
        print ("Resultado incorreto da matriz")
    else:
        print ("Resultado correto") 

def multiplicar_vetor(matriz, X, B, R):
    for i in range(n):
        j = 0
        c = 0
        k = X[c]* matriz[i][j] + X[c+1] * matriz[i][j+1]
        R.append(k)
    return (R)

#verifica a casa adjacente a posicao centro_linha/centro_coluna na matriz
def verificar_entorno_casa(matriz, centro_linha, centro_coluna, posicao):
    centro = matriz[centro_linha][centro_coluna]
    #posicoes adjacentes
    #0 == centro  
    #1|2|3
    #8|0|4
    #7|6|5  
    if(posicao == 1):
        return verificar_posicao_valida(matriz, centro_linha-1, centro_coluna-1)            
    if(posicao == 2):
        return verificar_posicao_valida(matriz, centro_linha-1, centro_coluna)  
    if(posicao == 3):
        return verificar_posicao_valida(matriz, centro_linha-1, centro_coluna+1)
    if(posicao == 4):
        return verificar_posicao_valida(matriz, centro_linha, centro_coluna+1)    
    if(posicao == 5):
        return verificar_posicao_valida(matriz, centro_linha+1, centro_coluna+1)
    if(posicao == 6):
        return verificar_posicao_valida(matriz, centro_linha+1, centro_coluna)    
    if(posicao == 7):
        return verificar_posicao_valida(matriz, centro_linha+1, centro_coluna-1)
    if(posicao == 8):
        return verificar_posicao_valida(matriz, centro_linha, centro_coluna-1)    

#verifica se a posicao dada e valida na matriz
def verificar_posicao_valida(matriz, linha, coluna):     
    if(linha < 0):
        return "Invalido"
    elif(linha >= len(matriz)):
        return "Invalido"
    elif(coluna < 0):
        return "Invalido"
    elif(coluna >= len(matriz[0])):
        return "Invalido"
    else:
        return matriz[linha][coluna]
