#
#introdução a programação de computadores
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
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
#  + Salário Bruto : R$
#  - IR (11%) : R$
#  - INSS (8%) : R$
#  - Sindicato ( 5%) : R$
#  = Salário Liquido : R$
#   Obs.: Salário Bruto - Descontos = Salário Líquido.
#

print ("Vamos calcular quanto voce ganha num mes?")
ganhos_horas = float(input("Insira quanto voce ganha por hora: "))
horas_trabalhadas = int(input("Insira a quantidade de horas trabalhadas: "))

salario = ganhos_horas * horas_trabalhadas
imposto_r = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
descontos = imposto_r + inss + sindicato
salario_liquido = salario - descontos

print ("Seu salario bruto e de R$%.2f, serao descontados R$%.2f para imposto de renda, R$%.2f para o INSS e R$%.2f para o sindicato.\nSeu salario liquido e de R$%.2f"%(salario, imposto_r, inss, sindicato, salario_liquido))
