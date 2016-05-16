#Introducao a programacao de computadores
#Professor: Jucimar Junior
#samuel silva de frança - 1615310049
#bruno de oliveira freire - 1615310030
#Felipe Henrique Bastos Costa - 1615310032
def analisar_Matriz(matriz,linha,coluna):
    cont = 1
    if(matriz[0][0] == 0 and  matriz[0][1] == 0 or  matriz[1][0] == 0):
        matriz[0][0] = cont
        cont+=1
    for i in range(linha):
        for j in range(coluna):            
            if(matriz[i][j] != -1 and matriz[i-1][j-1] != 0):
                matriz[i][j] = cont
                cont+=1

                    
    return matriz

def imprimir(matriz, linha):
    for i in range(linha):
        print(matriz[i])
        
matriz = [[0, 0, -1, 0], [-1, 0, -1, 0], [0, -1, 0, 0]]

imprimir((analisar_Matriz(matriz,3,3)),3)

