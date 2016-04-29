from matriz import*

def verificar_nulas (matriz,linha, coluna):
    ac_linha = 0
    ac_coluna = 0
    for i in range(linha):
        ac1 = 0
        ac2 = 0
        for j in range(coluna):
            if matriz[i][j] == 0:
                ac1 += 1
                if ac1 == linha:
                    ac_linha += 1
            if matriz[j][i] == 0:
                ac2 += 1
                if ac2 == coluna:
                    ac_coluna += 1
    return ("Numero de Linhas nulas %d, e numero de colunas nulas %d" %(ac_linha, ac_coluna))
m=int(input())
n=int(input())
matriz = []
matriz = gerar_matriz(m,n)
x = verificar_nulas(matriz,m,n)
print (x)
           
                
            
