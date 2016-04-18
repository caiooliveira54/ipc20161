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

n1 = int(input("Insira a primeira nota: "))
n2 = int(input("Insira a segunda nota: "))

media = (n1+n2)/2

if media == 10:
    print ("Aprovado com vantagem")
elif media >= 7:
    print ("Aprovado")
else:
    print ("Reprovado")
