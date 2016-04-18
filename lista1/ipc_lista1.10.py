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

c = float(input("Entre com a temperatura em graus Celsius : ")) # Solicita ao usuário a temperatura em celsius

vt = c * 1.8 # Multiplica a temperatura em celsius por 1.8 (Etapa da fórmula)
f = vt + 32 # Depois soma com 32 que é o resultado de celsius para farenheit

print ("A temperatura em Farenheit é: %.1f" %f) # Impressão da temperatura em farenheit para o usuário
