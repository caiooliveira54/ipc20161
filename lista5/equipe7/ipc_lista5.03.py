#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

#Questao3.  Dadas duas matrizes reais  Amxn e Bnxp, calcular o produto de A por B. 



def multiplicarmatriz(matrizA, matrizB, linhaA, colunaB):
    matrizR = []
    a = 0
    b = 0
    for i in range (linhaA):
        linha = []
        for j in range (colunaB): 
            mult = matrizA[i][a]* matrizB[a][j] + matrizA[i][a+1]* matrizB[a+1][j]
            linha.append(mult)
        matrizR.append(linha)
    return matrizR
   
def fazermatriz (linha, coluna):
    matriz =[]
    for i in range (1, linha+1):
        linha = []
        for j in range (1, coluna+1):
            num = int(input("Digite a posicao %i%i da matriz: " %(i,j)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def mostrarmatriz(matriz, linha, coluna):
    for i in range(linha):
        print (matriz[i])
        
m = int(input("Digite a quantidade de linhas da matriz: "))
n = int(input("Digite a quantidade de colunas da matriz: "))
A = []
A = fazermatriz (m,n)
print ("Matriz A:")
mostrarmatriz(A, m, n)

p = int(input("Digite a quantidade de colunas da matriz: "))
B = []
B = fazermatriz (n,p)
print ("Matriz B:")
mostrarmatriz(B, n, p)

C = []
C = multiplicarmatriz(A, B, m, p)
print ("Matriz produto:")
mostrarmatriz(C, m, p)