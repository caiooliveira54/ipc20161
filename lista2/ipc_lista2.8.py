#EQUIPE 2
# Ana Beatriz Faria Frota - 1615310027
# Nahan Trindade Passos - 1615310021
# 
#

p1 = float(input("informe o valor do primeiro produto: "))
p2 = float(input("informe o valor do segundo produto: "))
p3 = float(input("informe o valor do terceiro produto: "))

if p1<p2:
    if p1<p3:
        print ("você deve comprar o primeiro produto!")
if p2<p1:
    if p2<p3:
        print ("você deve comprar o segundo produto!")
if p3<p1:
    if p3<p2:
        print ("você deve comprar o terceiro produto!")
