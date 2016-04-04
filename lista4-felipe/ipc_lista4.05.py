#
#Programa Lista 4, questão 5;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista = [] # Vetor que receberá todos os valores inseridos no modo de entrada
par = [] # Vetor que receberá todos os números que são divisíveis por dois e resto zero, ou, pares
impar = [] # Vetor que receberá todos os números que são impares
v = 20 # Quantidade que limitará até onde o contador será incrementado
cont1 = 0 # Contador que será incrementado até a condição ser False
cont2 = 1 # Contador que mostrará qual número ele irá solicitar no 'input'

while(cont1 < v):
    x = int(input("Informe o %dº numero de sua lista de 20 números:\n"%cont2)) # Solicitará os 20 valores do vetor
    lista.append(x) # Adicionará todos os valores inseridos ao vetor
    if(lista[cont1]%2==0): # Condição para ser par
        par.append(x) 
    else: # Condição para ser ímpar
        impar.append(x)
    cont1+=1 # Incrementando o contador 1
    cont2+=1 # Incrementando o contador 2
print("A lista completa e:\n%s\nOs numeros pares sao:\n%s\nOs impares sao:\n%s"%(lista,par,impar))
