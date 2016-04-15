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
