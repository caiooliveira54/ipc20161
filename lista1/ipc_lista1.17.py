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
