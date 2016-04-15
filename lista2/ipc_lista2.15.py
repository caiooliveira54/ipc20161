#Equipe 2
#
#Ana Beatriz Frota - 1615310027
#Nahan Trindade Passos - 1615310021
#
#

lado1 = float(input("Tamanho do primeiro lado:\n"))
lado2 = float(input("Tamanho do segundo lado:\n"))
lado3 = float(input("Tamanho do terceiro lado:\n"))

if((lado1+lado2)>lado3):
    print("Triangulo")
    if(lado1 == lado2 and lado1==lado3):
        print("Equilatero")
    elif(lado1 == lado2 or lado1==lado3 or lado2==lado3):
        print("Isoceles")
    else:
        print("Escaleno")
else:
    print("Nao pode ser um triangulo")
