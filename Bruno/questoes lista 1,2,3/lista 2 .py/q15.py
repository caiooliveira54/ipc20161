lado1 = float(input("Indique o primeiro lado: "))
lado2 = float(input("Indique o segundo lado: "))
lado3 = float(input("Indique o terceiro lado: "))

if (lado1 + lado2 > lado3):
    if (lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
        print("Triangulo Equilatero")
    if (lado1 == lado2 and lado1 != lado3 ):
        print(" Triangulo isosceles ")
    if(lado1 == lado3 and lado1 != lado2):
        print(" Triangulo isosceles ")
    if(lado2 == lado3 and lado2 != lado1):
        print(" Triangulo isosceles ")
    if(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
        print(" Triangulo escaleno ")
else:
    print(" nao pode ser um triangulo ")
