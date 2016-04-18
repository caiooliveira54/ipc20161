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

altura  = float(input("Digite sua altura em metros, separa por ponto (ex: 1.60): ")) # Solicita a altura do usuário

vT = 72.7 * altura  # Etapa 1 do processo do cálculo do peso ideal
r = vT - 58 # # Etapa 2 do processo do cálculo do peso ideal

print ("Seu peso ideal e %.2f "%r) # Impressão do peso ideal do usuário
