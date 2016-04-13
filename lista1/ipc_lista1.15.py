#
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Matheus Henrique Araujo Batista - 1615310039
# Nahan Trindade Passos - 1615310021
# Victor Hugo Souza Correia - 1615310024
# 

print ("Vamos calcular quanto você ganha num mês?")
ganhos_horas = float(input("Insira quanto você ganha por hora: "))
horas_trabalhadas = int(input("Insira a quantidade de horas trabalhadas: "))

salario = ganhos_horas * horas_trabalhadas
imposto_r = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
descontos = imposto_r + inss + sindicato
salario_liquido = salario - descontos

print ("Seu salário bruto é de R$%.2f, serão descontados R$%.2f para imposto de renda, R$%.2f para o INSS e R$%.2f para o sindicato.\nSeu salário líquido é de R$%.2f"%(salario, imposto_r, inss, sindicato, salario_liquido))
