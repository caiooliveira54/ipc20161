#
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Matheus Henrique Araujo Batista - 1615310039
# Nahan Trindade Passos - 1615310021
# Victor Hugo Souza Correia - 1615310024
#

n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))
n3 = int(input("Insira mais outro número: "))

if n1>n2 and n1>n3:
    print ("O primeiro número é maior")
    if n2>n3:
        print ("O terceiro número é maior")
    else:
        print ("O segundo número é maior")
if n2>n1 and n2>n3:
    print ("O segundo número á maior")
    if n1>n3:
        print ("O terceiro número é menor")
    else:
        print ("O primeiro número é menor")
if n3>n1 and n3>n2:
    print ("O terceiro número é maior")
    if n1>n2:
        print ("O segundo número é menor")
    else:
        print ("O primeiro numero e menor")
