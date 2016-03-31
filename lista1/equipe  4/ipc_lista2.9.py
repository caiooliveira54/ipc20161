#
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Matheus Henrique Araujo Batista - 1615310039
# Nahan Trindade Passos - 1615310021
# Victor Hugo Souza Correia - 1615310024
#

n1 = int(input("Coloque um primeiro número: "))
n2 = int(input("Coloque um segundo número: "))
n3 = int(input("Coloque um terceiro número: "))

if n1>n2>n3:
    print (n1, n2, n3)
if n1>n3>n2:
    print (n1, n3, n2)
if n2>n1>n3:
    print (n2, n1, n3)
if n2>n3>n1:
    print (n2, n3, n1)
if n3>n1>n2:
    print (n3, n1, n2)
if n3>n2>n1:
    print (n3, n2, n1)
