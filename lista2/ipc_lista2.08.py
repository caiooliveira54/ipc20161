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
