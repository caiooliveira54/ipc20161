#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 1
#
#Any Mendes Carvalho - 1615310044
#Eduardo Maia Freire - 1615310003
#Kid Mendes de Oliveira Neto - 1615310011
#Luiz Gustavo de Rocha Melo - 1615310015
#Matheus Palheta Barbosa -1615310019
#Victor Rafael da Silva e Silva - 1615310025
#

n1 = int(input("Insira um numero: "))
n2 = int(input("Insira outro numero: "))
n3 = int(input("Insira mais um numero: "))

if n1>n2:
    if n1>n3:
        print ("O primeiro numero e maior")
if n2>n1:
    if n2>n3:
        print ("O segundo numero e maior")
if n3>n1:
    if n3>n2:
        print ("O terceiro numero e maior")
