#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

#Questao1. Dada uma matriz real A com m linhas e n colunas e um vetor real V com n elementos, determinar o produto de A por V. 

def multiplicarvetor(m,n):
    matrizR = []
    for i in range (m):
        linha = []
        for j in range (n):
            mul = A[i][j] * V [i]
            linha.append(mul)
        matrizR.append(linha)
    vetorR = []
    h = 0    
    for k in range(m):
        num = matrizR[k][h] + matrizR[k][h+1]
        vetorR.append(num)
    return vetorR

def fazermatriz (m,n):
    matriz =[]
    for i in range (1, m+1):
        linha = []
        for j in range (1, n+1):
            num = int(input("Digite a posicao %i%i da matriz: " %(i,j)))
            linha.append(num)
        matriz.append(linha)
    return matriz
        
def fazervetor(n):
    vetor = []
    for i in range (1, n+1):
        num = int (input("Digite o elemento %i do vetor: " %(i)))
        vetor.append(num)
    return vetor
      
def mostrarmatriz(m, n):
    for i in range(m):
        print (A[i])
        
        
        
m = int(input("Digite a quantidade de linhas da matriz: "))
n = int(input("Digite a quantidade de colunas da matriz: "))
A = []
A = fazermatriz (m,n)
mostrarmatriz(m, n)
        
r = 0
V = []
V = fazervetor(n)
print (V)

vetorR = []
vetorR = multiplicarvetor(m,n)
print ("Resultado final da multiplicacao", vetorR)
