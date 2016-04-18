#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 2
#
#Ana Beatriz Frota  - 1615310027 
#Ariel Guilherme Rocha Capistrano - 1615310029
#Frankilin Yuri Gonçaves dos santos - 1615310033
#Kylciane Cristiny Lopes Freitas - 1615310052
#Lucas Ferreira Soares - 1615310014
#Luiz Alexandre Oliveira de Souza - 1615310057
#Luiz Gustavo Rocha Melo - 1615310015
#Nahan Trindade Passos - 1615310021
#Samuel Silva França - 1615310049
#

nota1 = float(input("Primeira nota parcial:\n"))
nota2 = float(input("Segunda nota parcial:\n"))
nota3 = float(input("Terceira nota parcial:\n"))

media = (nota1+nota2+nota3)/3

if(10>media >= 7):
    print("Aprovado! %.2f"%media)
elif(media == 10):
    print("Aprovado com distincao!",media)
else:
    print("Reprovado %.2f"%media)
