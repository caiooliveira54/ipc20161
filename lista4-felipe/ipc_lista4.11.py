#
#Programa Lista 4, questão 11;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista1 = []
lista2 = []
lista3 = []
lista4 = []
v1 = 10
cont1 = 0
cont2 = 1

while(cont1 < v1):
    x1 = raw_input("Informe o %dº elemento a ser colocado na 1º lista:\n"%cont2)
    x2 = raw_input("Informe o %dº elemento a ser colocado na 2º lista:\n"%cont2)
    x3 = raw_input("Informe o %dº elemento a ser colocado na 3º lista:\n"%cont2)
    lista1.append(x1)
    lista2.append(x2)
    lista3.append(x3)
    lista4.append(x1)
    lista4.append(x2)
    lista4.append(x3)
    cont1+=1
    cont2+=1

print("A uniao das listas de forma alternada e:\n%s"%lista4)