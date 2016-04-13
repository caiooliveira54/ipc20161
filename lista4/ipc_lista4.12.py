#1615310013
#Lorene Marques
i = []
a = []
x = 0
altacm = 0
c = 0
baixo = 0
while x < 5:
    idade = int(input("Informe a idade: "))
    altura = float(input("Informe a altura: "))
    i.append(idade)
    a.append(altura)
    altacm = altacm + altura
    x += 1

altmedia = altacm/5
while c < len(i):
    if i[c] > 12:
        if a[c] < altmedia:
            baixo = baixo + 1
    c += 1
            
print("Altura média: %2.2f"%altmedia)
print("%d alunos mais baixos que a média."%baixo)
