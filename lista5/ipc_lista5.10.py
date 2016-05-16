#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Kid Mendes de Oliveira Neto - 1615310011
#Eduardo Maia Freire - 1615310003
#Igor Menezes Sales Vieira - 1615310007
#

def tabuleiro(matriz):
    contPecasBrancas = 0
    contSemPecas = 0
    contNaoMove = 0
    #Se move sem capturar peças
    for i in range(7):
        for j in range(7):
            if(matriz[i][j] == -1):
                if(matriz[i+1][j-1] == 0):
                    contSemPecas += 1
                elif(matriz[i+1][j+1] == 0):
                    contSemPecas += 1

   #Se move e captura peças brancas
    for i in range(7):
        for j in range(7):
            if(matriz[i][j] == -1):
                if(matriz[i+1][j-1] == 1):
                    contPecasBrancas += 1
                    matriz[i+1][j-1] = 0
                elif(matriz[i+1][j+1] == 1):
                    contPecasBrancas += 1
                    matriz[i+1][j+1] = 0
    #Não se move
    for i in range(8):
        for j in range(8):
            if(matriz[i][j] == -1):
                if(matriz[i+1][j-1] == -1):
                    contNaoMove +=1
                elif(matriz[i+1][j+1] == -1):
                    contNaoMove +=1
    
    return contPecasBrancas,contNaoMove,contSemPecas
def exibir_tabuleiro(matriz):
    for i in range(8):
        print(matriz[i])
        
matriz = [[-1,0,-1,0,-1,0,-1,0],[0,-1,0,-1,0,-1,0,-1],[-1,0,-1,0,-1,0,-1,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1]]
exibir_tabuleiro(matriz)
print(tabuleiro(matriz))

'''Monitor: Gabriel Alonso
Membros: Kid Mendes de Oliveira Neto
Eduardo Maia Freire
Igor Menezes Sales Vieira''' 
