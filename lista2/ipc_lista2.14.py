#
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Matheus Henrique Araujo Batista - 1615310039
# Nahan Trindade Passos - 1615310021
# Victor Hugo Souza Correia - 1615310024
#

print ("Vamos saber se você foi aprovado! \nPrimeiramente...")
n1 = float(input("Insira sua primeira nota: "))
n2 = float(input("Insira sua segunda nota: "))
media = (n1+n2)/2

if 9>=media>=10:
    print (n1)
    print (n2)
    print (media)
    print ("Conceito A")
    print ("Aprovado")
elif 9>media>=7.5:
    print (n1)
    print (n2)
    print (media)
    print ("Conceito B")
    print ("Aprovado")
elif 7.5>media>=6.0:
    print (n1)
    print (n2)
    print (media)
    print ("Conceito C")
    print ("Aprovado")
elif 6.0>media>=4.0:
    print (n1)
    print (n2)
    print (media)
    print ("Conceito D")
    print ("Reprovado")
elif 4.0>media>0.0:
    print (n1)
    print (n2)
    print (media)
    print ("Conceito E")
    print ("Reprovado")
else:
    print ("Conceito E")
    print ("Reprovado")
