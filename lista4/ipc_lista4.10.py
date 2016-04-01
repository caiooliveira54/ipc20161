lista1 = []
lista2 = []
lista3 = []
v1 = 10
cont1 = 0
cont2 = 1

while(cont1 < v1):
    x1 = raw_input("Informe o %dº elemento a ser colocado na primeira lista:\n"%cont2)
    x2 = raw_input("Informe o %dº elemento a ser colocado na segunda lista:\n"%cont2)
    lista1.append(x1)
    lista2.append(x2)
    lista3.append(x1)
    lista3.append(x2)
    cont1+=1
    cont2+=1

print("A uniao das listas de forma alternada e:\n%s"%lista3)