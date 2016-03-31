#
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Matheus Henrique Araujo Batista - 1615310039
# Nahan Trindade Passos - 1615310021
# Victor Hugo Souza Correia - 1615310024
#

n1 = int(input("Insira a primeira nota: "))
n2 = int(input("Insira a segunda nota: "))
media = (n1+n2)/2
if media == 10:
    print ("Aprovado com distinção")
elif media >= 7:
    print ("Aprovado")
else:
    print ("Reprovado")
