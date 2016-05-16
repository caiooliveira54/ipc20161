#Introducao a programacao de computadores
#Professor: Jucimar Junior
#samuel silva de frança - 1615310049
#bruno de oliveira freire - 1615310030
#Felipe Henrique Bastos Costa - 1615310032
#Monitor: Wilson Calisto, Lucas Botinelly e Delrick Oliveira

def criar_exemplo():
    tabuleiro = [[-1,0,-1,0,-1,0,-1,0],[0,-1,0,-1,0,-1,0,-1],[-1,0,-1,0,0,0,0,0],[0,0,0,0,0,0,0,-1],[0,0,0,0,1,0,-1,0],[0,1,0,0,0,1,0,0],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1]]
    return tabuleiro
def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print matriz[i]

def analisar_verdade(matriz, linha, coluna):     
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

def verificar_tomar_pecas(matriz):
    pecas = []
    for i in range(8):
        for j in range(8):
            lista = []
            if matriz[i][j] == -1 and analisar_verdade(matriz,i+1,j+1) != "Invalido" or analisar_verdade(matriz,i+2,j+2) != "Invalido":
                if matriz[i][j] == -1 and matriz[i+1][j+1] == 1 and matriz[i+2][j+2] == 0:
                    lista.append(i)
                    lista.append(j)
            if matriz[i][j] == -1 and analisar_verdade(matriz,i+1,j-1) != "Invalido" or analisar_verdade(matriz,i+2,j-2) != "Invalido":
                if matriz[i][j] == -1 and matriz[i+1][j-1] == 1 and matriz[i+2][i-2] == 0:
                    lista.append(i)
                    lista.append(j)
        if len(lista) > 0: 
            pecas.append(lista)
    if len(pecas) == 0:
        pecas = "Nao tem"
    return pecas

def verificar_mover(matriz):
    pecas = []
    for i in range(8):
        for j in range(8):
            lista = []
            for k in range(2):
                if matriz[i][j] == -1 and analisar_verdade(matriz,i+1,j-1) != "Invalido" or analisar_verdade(matriz,i+1,j+1) != "Invalido" and k == 0:
                    if matriz[i][j] == -1 and matriz[i+1][j-1] == 0:
                        lista.append(i)
                        lista.append(j)
                        break
                if matriz[i][j] == -1 and analisar_verdade(matriz,i+1,j+1) != "Invalido" and k == 1:
                    if matriz[i][j] == -1 and matriz[i+1][j+1] == 0:
                        lista.append(i)
                        lista.append(j)
                        break
            if len(lista) > 0:        
                pecas.append(lista)
    if len(pecas) == 0:
        pecas = "Nao tem"        
    return pecas

def verificar_imobilidade(matriz):
    pecas = []
    for i in range(8):
        for j in range(8):
            lista = []
            if matriz[i][j] == -1 and analisar_verdade(matriz,i+1,j+1) == "Invalido" or analisar_verdade(matriz,i+2,j+2) == "Invalido" or analisar_verdade(matriz,i+1,j-1) == "Invalido" or analisar_verdade(matriz,i+2,j-2) == "Invalido":
                lista.append(i)
                lista.append(j)          
            else:
                if matriz[i][j] == -1 and matriz[i+1][j+1] == 1 and matriz[i+2][j+2] == 1 or matriz[i+1][j-1] == 1 and matriz[i+2][j-2] == 1:
                    lista.append(i)
                    lista.append(j)
            if len(lista) > 0:
                pecas.append(lista)
    if len(pecas) == 0:
        pecas = "Nao tem"    
    return pecas

tabuleiro = criar_exemplo()
mostrar_matriz(tabuleiro)
a = verificar_tomar_pecas(tabuleiro)
b = verificar_mover(tabuleiro)
c = verificar_imobilidade(tabuleiro)
print("\nRespostas:\na) %s\nb) %s\nc) %s"%(a,b,c))