#
#Programa Lista 4, questão 14;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista = []
cont = 0

a = raw_input("Telefonou para a vítima?\n")
b = raw_input("Esteve no local do crime?\n")
c = raw_input("Mora perto da vítima?\n")
d = raw_input("Devia para a vítima?\n")
e = raw_input("Já trabalhou com a vítima?\n")

lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)

for i in range(5):
    if(lista[i] == "Sim" or lista[i] == "sim"):
        cont += 1
if(cont < 2):
    print("Inocente")
elif(cont == 2):
    print("Suspeita")
elif(cont > 2 and cont < 5):
    print("Cumplice")
else:
    print("Assassino")