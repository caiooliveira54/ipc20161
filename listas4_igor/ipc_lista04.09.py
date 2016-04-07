#
#Igor Menezes Sales Vieira - Matricula: 1615310007
#
A = [] #Vetor A pedido
soma = 0 #Variavel da soma
quadrado = 1 #Variavel do Quadrado a ser somado

for i in range(10): #Pedir ao usuario ate chegar no decimo indice
    numerox = int(input("Informe o numero: ")) #Nova variavel a ser inserida na lista
    A.append(numerox) #Insercao da nova variavel na lista do vetor A

for i in A:
    quadrado = i**2 #Valor do quadrado
    soma = soma+quadrado #Valor da soma

print("A soma dos quadrados e: %d"%soma) #Imprime o valor da soma
