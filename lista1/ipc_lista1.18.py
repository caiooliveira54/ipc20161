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

tamanho = float(input("Tamanho do arquivo em mb:\n"))
velocidade = float(input("Velocidade do link:\n"))

tempo = (tamanho)/(velocidade/60)

print("Tempo estimado:",tempo)
