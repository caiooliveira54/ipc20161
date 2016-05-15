#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

#Questao 2. Um vetor real X com n elementos � apresentado como resultado de um sistema de equa��es lineares Ax = B cujos coeficientes s�o representados em uma matriz real Amxn e os lados direitos das equa��es em um vetor real B de m elementos. Verificar se o vetor X � realmente solu��o do sistema dado.
 
def verificar(matriz, R):
    if R != B:
        print ("Resultado incorreto da matriz")
    else:
        print ("Resultado correto") 

def multiplicar_vetor(matriz, X, B, R):
    for i in range(n):
        j = 0
        c = 0
        k = X[c]* matriz[i][j] + X[c+1] * matriz[i][j+1]
	R.append(k)
    return (R)
def gerar_vetor(n):
    vetor = []
    for i in range(n):
        num = int(input("V(%d): \t"%(i)))
        vetor.append(num)
    return vetor

def mostrar_matriz(matriz, m):
	for i in range(m):
	    print(matriz[i])
		
def gerar_matriz(m, n):
    matriz = []
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            num = int(input("A(%d%d):\t"%(i, j)))
            linha.append(num)
        matriz.append(linha)
    return matriz


matriz = []  
m = int(input("Digite o numero de linhas da matriz: "))
n = int(input("Digite o numero de colunas da matriz: "))
matriz = gerar_matriz(m,n)
mostrar_matriz(matriz, m)

print ("Vetor de resultados: ")
X = []
X = gerar_vetor(n)
print (X)

print ("Vetor de termos independentes: ")
B = []
B = gerar_vetor(n)
print(B)

print ("Multiplicacao do sistema")
R = []
R = multiplicar_vetor(matriz, X, B, R)
print(R)

print ("Verificacao de resultado")
verificar(matriz, R)