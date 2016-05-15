#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 5
#
#Ariel Guilherme Rocha Capistrano - 1615310029
#

def criar_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            numero = int(input("linha %d,coluna %d:"%(i+1,j+1)))
            linha.append(numero)
        matriz.append(linha)
    return matriz

def criar_vetor(coluna):
    vetor = []
    for i in range(coluna):
        numero = int(input("Vetor coluna %d:"%(i+1)))
        vetor.append(numero)
    print("vetor")
    print(vetor)
    return vetor

def mostrar_matriz(matriz,linha):
    print("matriz")
    for i in range(linha):
        print(matriz[i])

def multiplicar_linhavetor(matriz,vetor):
    linha = len(matriz)
    coluna = len(matriz[0])
    resultado = []
    for i in range(linha):
        acm = 0
        for j in range(coluna):
            acm += matriz[i][j] * vetor[j]
        resultado.append(acm)
    print("multiplicando")
    print(resultado)

def multiplicar_matriz(matriz_a,matriz_b):
    linha_a = len(matriz_a)
    coluna_a = len(matriz_a[0])
    linha_b = len(matriz_b)
    coluna_b = len(matriz_b[0])
    resultado = []
    for i in range(linha_a):
        linha = []
        for j in range(coluna_b):
            acm = 0
            for k in range(linha_b):
                acm += matriz_a[i][k]*matriz_b[k][j]
            linha.append(acm)
        resultado.append(linha)
    return resultado

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
