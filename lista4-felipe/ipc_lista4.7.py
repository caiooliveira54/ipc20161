#
#Programa Lista 4, questão 7;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista = []
v = 5
cont1 = 0
cont2 = 1
soma = 0
multiplicacao = 1

while(cont1 < v):
    x = int(input("Informe o numero inteiro que deseja por na sua lista:\n"))
    lista.append(x)
    soma += x
    multiplicacao *= x
    cont1 += 1
    cont2 += 1
print("A soma dos numeros e %d\nA multiplicacao e %d\nA lista como um todo e %s"%(soma,multiplicacao,lista))