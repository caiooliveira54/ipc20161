#
#Programa Lista 4, questão 9;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista = [] # Vetor que receberá os 10 números
v = 10 # Limite para o contador
cont1 = 0 
cont2 = 1
soma = 0 # Acumulador para somar os números
while(cont1 < v):
    x = int(input("Informe o %dº numero inteiro da sua lista:\n"%cont2)) # Solicitará os valores enquanto for 'True'
    lista.append(x) # Adicionará ao vetor os numeros
    soma = soma + (x**2) # Elevará os números ao quadrado
    cont1+=1
    cont2+=1
print(soma) # Imprimirá a soma dos quadrados
