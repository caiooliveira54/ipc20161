#
#Igor Menezes Sales Vieira - Matricula: 1615310007
#
consoantes = []
letras = []
acm = 0
for i in range(1,11):
    letra = input("Digite letra em aspas:")
    letras.append(letra)
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        acm = acm
    else:
        acm = acm + 1
        consoantes.append(letra)

print("%d consoantes foram lidas.\n Elas sao as seguintes: %s"%(acm, consoantes))
