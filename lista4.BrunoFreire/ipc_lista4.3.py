#Bruno de Oliveira Freire - 1615310030
nota=[0,0,0,0]
soma=0
qtd=4
cont=0
media=0

while cont<4:
    nota[cont]=float(input("insira uma nota:"))
    soma=soma+nota[cont]
    cont+=1
media=soma/qtd
print(nota)
print("essa e a media:%.1f"%media)