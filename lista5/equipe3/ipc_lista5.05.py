#Introducao a programacao de computadores
#Professor: Jucimar Junior
#samuel silva de frança - 1615310049
#bruno de oliveira freire - 1615310030
#Felipe Henrique Bastos Costa - 1615310032
def criar_matriz(linha,coluna):
    matriz=[]
    for i in range(linha):
        matriz.append([])
        for j in range(coluna):
            numero=int(input("digite o numero a ser colocado na matriz:"))
            matriz[i].append(numero)
    return matriz

def verificar_permutacao(linha,coluna,matriz):
    for i in range(linha):
        ac=0
        ac2=0
        for j in range(coluna):
            if matriz[i][j]==0 or matriz[i][j]==1:
                if matriz[i][j]==1:
                    ac+=1
                if matriz[j][i]==0:
                    ac2+=1
            else:
                print "não é uma matriz de permutacão"
    if ac==1 and ac2==1:
        print "R: e de permutacao"
    else:
        print("R: nao e de permutacao")
        
def mostrar_matriz(linha,matriz):
    for i in range(linha):
        print matriz[i]
    
            
linha=int(input("digite a quantidade de linhas:"))
coluna=int(input("digite a quantidade de colunas:"))
matrizA=criar_matriz(linha,coluna)
print "---------------------Matriz-----------------------"
mostrar_matriz(linha,matrizA)
print "-------------    Essa matriz:   ---------------"
verificar_permutacao(linha,coluna,matrizA)
            
        
                        