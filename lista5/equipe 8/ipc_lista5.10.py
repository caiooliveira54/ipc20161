#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Matheus Palheta Barbosa - 1615310019
#Any Mendes Carvalho - 1615310044
#Victor Rafael da Silva e Silva - 1615310025
#

from matriz import*
            # 0  1  2  3  4  5  6  7
tabuleiro = [[0, 0, 0, 0, 0, 0, 0, 0], # 0
             [0, 0, 0, 0, 0, 0, 0, 0], # 1
             [0, 0, 0, 0, 0, 0, 0, 0], # 2
             [0, 0, 0, 0, 0, 0, 0, 0], # 3
             [0, 0, 0, 0, 0, 0, 0, 0], # 4
             [0, 0, 0, 0, 0, 1, 0, 0], # 5
             [0, 0, 0, 0, 1, 0, 0, 0], # 6
             [0,-1, 0,-1, 0,-1, 0,-1],]# 7

def verificar_movimento_peca(matriz, linha, coluna):
    print("peca posicao (%d,%d)" % (linha, coluna))
    
    pode_mover = False;
    
    if(verificar_entorno_casa(matriz, linha, coluna, 1) == 0):
        print("Pode se mover para diagonal esquerda")
        pode_mover = True;
    if(verificar_entorno_casa(matriz, linha, coluna, 3) == 0):
        print("Pode se mover para diagonal direita")
        pode_mover = True;
    if(verificar_entorno_casa(matriz, linha, coluna, 1) == 1):
        if(verificar_entorno_casa(matriz, linha-1, coluna-1, 1) == 0):
            print("Pode se comer peca branca para diagonal esquerda")    
            pode_mover = True;
    if(verificar_entorno_casa(matriz, linha, coluna, 3) == 1):
        if(verificar_entorno_casa(matriz, linha-1, coluna+1, 3) == 0):
            print("Pode se comer peca branca para diagonal direita")     
            pode_mover = True;
    
    if(not(pode_mover)):
        print("nao pode se mover")

for linha in range(len(tabuleiro)):
    for coluna in range(len(tabuleiro[0])):
        if(tabuleiro[linha][coluna] == -1):
            verificar_movimento_peca(tabuleiro, linha, coluna);