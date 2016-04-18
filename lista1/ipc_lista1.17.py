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

import math # Importando a biblioteca matemática

area = float(input("Area em metros:\n")) # Solicita ao usuário a quantidade em metros a ser pintada
litros = area/6 # Aqui calcula a quantidade em litros necessária

qtdlatas = litros/18 # Processamento da quantidade de litros a ser utilizados sobre a quantidade de litros de uma lada que determinará a quantidade de latas
qtdlatasF = round(qtdlatas) # Caso seja um número de ponto flutuante, arredondará o valor
valor_latas = qtdlatasF*80 # Aqui calculará o preço total pago pelas latas

print("A quantidade de latas sera de:%d"%qtdlatasF) # Imprime a quantidade de latas a serem compradas  
print("O valor a ser pago pelas latas sera de:%d"%valor_latas) # Imprime o preço das latas a serem compradas

qtdgalao = litros/3.6 # Processamento de quantidade de litros a ser utilizado sobre a quantidade de litros de um galao que determinará a quantidade de galões
qtdgalaoF = round(qtdgalao) # Caso seja um número de ponto flutuante, arredondará o valor 
valor_galao = qtdgalaoF*25 # Calculo do preço pago pelos galões 

print("A quantidade de galoes sera de:%d"%qtdgalaoF)# Aqui imprimirá a quantidade de galões necessárias
print("O valor de galao e:%d"%valor_galao) # Aqui imprimirá ao usuário o valor total dos galões

restolata = (litros % 18)
restogalao = round(restolata/3.6)

print("A quantidade de latas sera de:", int(qtdlatas),"e a de galoes sera: %d"%restogalao)
print("O valor gasto das latas:",valor_latas,"e o de galoes:",valor_galao)
