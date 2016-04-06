lista=[]
cont=0

a= raw_input("telefonou para a vitima?\n")
b= raw_input("esteve no local do crime? \n")
c= raw_input("Mora perto da vitima? \n")
d= raw_input("Devia para a vitima? \n")
e= raw_input("ja trabalhou com a vitima? \n")

lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)

for i in range(5):
    if lista[i]=="sim":
        cont+=1
print("---------------------------------")
if cont==2 :
    print("voce e Suspeita")
elif cont==3 or cont==4:
    print("voce e cumplice")
elif cont==5:
    print("voce e assassino")
        

