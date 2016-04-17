#
#Introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 1
#
#Any Mendes Carvalho - 1615310044
#Kid Mendes de Oliveira Neto - 1615310011
#Victor Rafael da Silva e Silva - 1615310025
#Eduardo Maia Freire - 1615310003
#Luiz Gustavo de Rocha Melo - 1615310015
#Matheus Palheta Barbosa -1615310019
#
#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#    comprar apenas latas de 18 litros;
#    comprar apenas galões de 3,6 litros;
#    misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 
#

import math

area = float(input("Area em metros:\n"))
litros = area/6

qtdlatas = litros/18
qtdlatasF = round(qtdlatas)
valor_latas = qtdlatasF*80

print("A quantidade de latas sera de:%d"%qtdlatasF)
print("O valor a ser pago pelas latas sera de:%d"%valor_latas)

qtdgalao = litros/3.6
qtdgalaoF = round(qtdgalao)
valor_galao = qtdgalaoF*25

print("A quantidade de galoes sera de:%d"%qtdgalaoF)
print("O valor de galao e:%d"%valor_galao)

restolata = (litros % 18)
restogalao = round(restolata/3.6)

print("A quantidade de latas sera de:", int(qtdlatas),"e a de galoes sera: %d"%restogalao)
print("O valor gasto das latas:",valor_latas,"e o de galoes:",valor_galao)
