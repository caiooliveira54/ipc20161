#
#Igor Menezes Sales Vieira 1615310007 
#Kid Mendes de Oliveira Neto 1615310011
#Victor Rafael da Silva e Silva 1615310025
#Josue Vasques Catachunga 1615310054
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
