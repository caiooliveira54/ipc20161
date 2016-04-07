#Nickso Patrick Façanha Calheiros - 1615310059

nota = [6,10,10,6]
c = 0
v = len (nota)
soma = 0
while c < v:
    print ("Nota na avaliçao:",nota[c])
    soma = soma + nota[c]
    c = c + 1
media = soma / c
print ("Sua media e: %2.2f" %media)
