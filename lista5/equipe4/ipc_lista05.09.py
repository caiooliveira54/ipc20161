#Introdução a programação de computadores
#Professor: Jucimar Junior
#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Luiz Gustavo de Rocha Melo - 1615310015

from matriz import*

def formatar_caca_palavra(matriz):
    numero_de_palavras = 0
    for i in range(len(matriz)):
        linha = matriz[i]
        for j in range(len(linha)):
            if(matriz[i][j] == 0):
                if(verificar_entorno_casa(matriz, i,j,8) == -1 or verificar_entorno_casa(matriz, i,j,8) == "Invalido"):
                    if(verificar_entorno_casa(matriz, i,j,4) == 0):
                        numero_de_palavras += 1
                        matriz[i][j] = numero_de_palavras
            if(matriz[i][j] == 0):
                if(verificar_entorno_casa(matriz, i,j,2) == -1 or verificar_entorno_casa(matriz, i,j,2) == "Invalido"):
                    if(verificar_entorno_casa(matriz, i,j,6) == 0):
                        numero_de_palavras += 1
                        matriz[i][j] = numero_de_palavras    

def gerar_matriz_exemplo():
    matriz_exemplo = gerar_matriz_vazia(5,8)
    matriz_exemplo[0][1] = -1
    matriz_exemplo[0][3] = -1
    matriz_exemplo[0][4] = -1
    matriz_exemplo[0][6] = -1
    matriz_exemplo[1][4] = -1
    matriz_exemplo[2][2] = -1
    matriz_exemplo[2][3] = -1
    matriz_exemplo[2][6] = -1
    matriz_exemplo[3][0] = -1
    matriz_exemplo[3][5] = -1
    matriz_exemplo[4][2] = -1
    matriz_exemplo[4][6] = -1
    matriz_exemplo[4][7] = -1
    return matriz_exemplo

caca_palavra = gerar_matriz_exemplo()
formatar_caca_palavra(caca_palavra)
print mostrar_matriz(caca_palavra, 5)
