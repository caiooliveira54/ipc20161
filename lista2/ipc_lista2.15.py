#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 2
#
#Ana Beatriz Frota  - 1615310027 
#Kylciane Cristiny Lopes Freitas - 1615310052
#Frankilin Yuri Gonçaves dos santos - 1615310033
#Lucas Ferreira Soares - 1615310014
#Luiz Gustavo Rocha Melo - 1615310015
#Nahan Trindade Passos - 1615310021
#Samuel Silva França - 1615310049
#Luiz Alexandre Oliveira de Souza - 1615310057
#Ariel Guilherme Rocha Capistrano - 1615310029
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
