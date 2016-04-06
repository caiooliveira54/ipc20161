ganho_por_h = float(input("Informe quanto você ganha por hora:\n"))
horas_mes = float(input("Informe quantas horas você trabalha no mês:\n"))

salario_bruto = ganho_por_h * horas_mes
inss = salario_bruto * 8/100
sindicato = salario_bruto * 5/100
imposto_renda = salario_bruto * 11/100
salario_liquido = salario_bruto - inss - sindicato - imposto_renda

print("+ Salario bruto:R$ %.2f"%salario_bruto)
print("- Imposto Renda:R$ %.2f"%imposto_renda)
print("- INSS:R$ %.2f"%inss)
print("- Sindicato:R$ %.2f"%sindicato)
print("= Salario liquido:R$ %.2f"%salario_liquido)
print("Obrigado!!!")