#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Gonçalves dos Santos - 1615310033

#Um vetor real X com n elementos é apresentado como resultado de um sistema de equações lineares Ax = B cujos coeficientes são representados em uma matriz real Amxn e os lados direitos das equações em um vetor real B de m elementos. Verificar se o vetor X é realmente solução do sistema dado.
 
from matriz import*  

matriz = []  
m = int(input("Digite o numero de linhas da matriz"))
n = int(input("Digite o numero de colunas da matriz"))
gerar_matriz(m,n)
mostrar_matriz(matriz, linhas)

print ("Vetor de resultados: ")
X = []
gerar_vetor(n)
print (X)

print ("Vetor de termos independentes: ")
B = []
gerar_vetor(n)
print(B)

print ("Multiplicacao do sistema")
R = []
multiplicar_vetor(matriz, X, B, R)
print(R)

print ("Verificacao de resultado")
verificar(matriz, R)
