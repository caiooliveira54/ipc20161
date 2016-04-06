lista = []
cont = 0
print("Responda Sim ou Nao: ")

a = raw_input("Telefonou para a vitima?  ")
b = raw_input("Esteve no local do crime?")
c = raw_input("Mora perto da vitima? ")
d = raw_input("Devia para a vitima? ")
e = raw_input("Ja trabalhou com a vitima? ")

lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)

for i in range(5):
    if lista[i] == "Sim" or lista[i] == "sim":
        cont = cont+1
if(cont<2):
    print("Inocente")
elif(cont==2):
    print("Suspeito")
elif(cont>2 and cont<5):
    print("Cumplice")
elif(cont==5):
    print("Assassino")
    
