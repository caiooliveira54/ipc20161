#
#Igor Menezes Sales Vieira - Matricula: 1615310007
#
idade = []
altura = []
idadeinv = []
alturainv = []

for i in range(1,6):
    idadex = int(input("Idade: "))
    alturax = float(input("Altura: "))
    idade.append(idadex)
    altura.append(alturax)

i = len(idade) - 1
while i >= 0:
    idadeinv.append(idade[i])
    i = i-1

i = len(altura) -1
while i >= 0:
    alturainv.append(altura[i])
    i = i-1

print(idadeinv)
print(alturainv)
    
