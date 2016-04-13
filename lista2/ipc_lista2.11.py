#
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Matheus Henrique Araujo Batista - 1615310039
# Nahan Trindade Passos - 1615310021
# Victor Hugo Souza Correia - 1615310024
#

print ("Quanto que será o reajuste de seu salário?")
salario_i = float(input("Insira o salário do colaborador atualmente: "))

if (salario_i<=280.00):
    aumento = salario_i * 0.20
    salario_f = salario_i + aumento
    print(" Salario inicial R$%.2f\n Porcentagem de 0.20\n Valor do aumento R$%.2f\n Salário final de R$%0.2f"%(salario_i, aumento, salario_f))
elif (280.00<salario_i<=700.00):
    aumento = salario_i * 0.15
    salario_f = salario_i + aumento
    print(" Salario inicial R$%.2f\n Porcentagem de 0.15\n Valor do aumento R$%.2f\n Salário final de R$%0.2f"%(salario_i, aumento, salario_f))
elif (700.00<salario_i<1500.00):
    aumento = salario_i * 0.10
    salario_f = salario_i + aumento
    print(" Salario inicial R$%.2f\n Porcentagem de 0.10\n Valor do aumento R$%.2f\n Salário final de R$%0.2f"%(salario_i, aumento, salario_f))
else:
    aumento = salario_i * 0.05
    salario_f = salario_i + aumento
    print(" Salario inicial R$%.2f\n Porcentagem de 0.05\n Valor do aumento R$%.2f\n Salário final de R$%0.2f"%(salario_i, aumento, salario_f))
