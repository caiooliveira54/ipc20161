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

print ("Vamos calcular quanto voce ganha num mes?") # Impressão de mensagem ao usuário
ganhos_horas = float(input("Insira quanto voce ganha por hora: ")) # Solicitará os ganhos por hora 
horas_trabalhadas = int(input("Insira a quantidade de horas trabalhadas: ")) # Solicitará a quantidade de horas trabalhadas

salario = ganhos_horas * horas_trabalhadas # Calculará o salário
imposto_r = salario * 0.11 # Calculará o destinado ao imposto de renda
inss = salario * 0.08 # Calculará o destinado ao INSS
sindicato = salario * 0.05 # Calculará o destinado ao sindicato
descontos = imposto_r + inss + sindicato # Os descontos do salário final
salario_liquido = salario - descontos # O valor a ser recebido

print ("Seu salario bruto e de R$%.2f, serao descontados R$%.2f para imposto de renda, R$%.2f para o INSS e R$%.2f para o sindicato.\nSeu salario liquido e de R$%.2f"%(salario, imposto_r, inss, sindicato, salario_liquido)) # Impressão de todos os valores calculados na etapa de processamento
