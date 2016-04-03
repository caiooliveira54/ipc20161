#
#Programa Lista 4, questão 9;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista = []
v = 10
cont1 = 0
cont2 = 1
soma = 0
while(cont1 < v):
    x = int(input("Informe o %dº numero inteiro da sua lista:\n"%cont2))
    lista.append(x)
    soma = soma + (x**2)
    cont1+=1
    cont2+=1
print(soma)
