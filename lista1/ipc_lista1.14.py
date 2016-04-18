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

peso = float(input("Informe o peso dos peixes: "))

if (peso > 50):
    excesso = peso - 50
    multa = excesso * 4.00
    print("Você excedeu" ,excesso, "kg do numero permitido de peixes \n  O valor \de sua multa e de R$",multa)

else:
    print("Voce nao excedeu o limite de peixes pescados")
