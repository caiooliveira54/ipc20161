#
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Matheus Henrique Araujo Batista - 1615310039
# Nahan Trindade Passos - 1615310021
# Victor Hugo Souza Correia - 1615310024
#

print ("Insira os valores abaixo para calcular a folha de pagamento")
ganhos_h = int(input("Quanto você ganha por hora? "))
horas_t = int(input("Quantas horas você trabalha? "))
salario = (ganhos_h * horas_t)

if (salario<=900):
    imposto_renda = 0.00
    sindicato = salario * 0.03
    inss = salario * 0.10
    fgts = salario * 0.11
    descontos = sindicato + inss
    salario_liquido = salario - descontos
    print(" Salário bruto R$%.2f \n IR R$%.2f \n INSS R$%.2f \n FGTS R$%.2f \n Desconto total R$%.2f \n Salário líquido R$%.2f" %(salario, imposto_renda, inss, fgts, descontos, salario_liquido))
    
elif (900<salario<=1500):
    imposto_renda = salario * 0.05
    sindicato = salario * 0.03
    inss = salario * 0.10
    fgts = salario * 0.11
    descontos = imposto_renda + sindicato + inss
    salario_liquido = salario - descontos
    print(" Salário bruto R$%.2f \n IR R$%.2f \n INSS R$%.2f \n FGTS R$%.2f \n Desconto total R$%.2f \n Salário líquido R$%.2f" %(salario, imposto_renda, inss, fgts, descontos, salario_liquido))
elif (1500<salario<=2500):
    imposto_renda = salario * 0.10
    sindicato = salario * 0.03
    inss = salario * 0.10
    fgts = salario * 0.11
    descontos = imposto_renda + sindicato + inss
    salario_liquido = salario - descontos
    print(" Salário bruto R$%.2f \n IR R$%.2f \n INSS R$%.2f \n FGTS R$%.2f \n Desconto total R$%.2f \n Salário líquido R$%.2f" %(salario, imposto_renda, inss, fgts, descontos, salario_liquido))
elif (salario>2500):
    imposto_renda = salario * 0.20
    sindicato = salario * 0.03
    inss = salario * 0.10
    fgts = salario * 0.11
    descontos = imposto_renda + sindicato + inss
    salario_liquido = salario - descontos
    print(" Salário bruto R$%.2f \n IR R$%.2f \n INSS R$%.2f \n FGTS R$%.2f \n Desconto total R$%.2f \n Salário líquido R$%.2f" %(salario, imposto_renda, inss, fgts, descontos, salario_liquido))
