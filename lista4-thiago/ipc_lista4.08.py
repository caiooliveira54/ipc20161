idade = []
altura = []
idadeinv = []
alturainv = []

for i in range(1,4):
    id_pessoa = int(input("Informe sua idade->"))
    alt_pessoa = float(input("Inform sua altura(m)->"))
    idade.append(id_pessoa)
    altura.append(alt_pessoa)

i = len(idade) - 1
while i >= 0:
    indice = idade[i]
    idadeinv.append(indice)
    i = i - 1

i = len(altura) - 1
while i >= 0:
    indice = altura[i]
    alturainv.append(indice)
    i = i - 1

print(idade)    
print(idadeinv)
print("\n",altura)
print(alturainv)
