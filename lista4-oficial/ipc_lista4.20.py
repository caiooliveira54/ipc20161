funcionarios = []
total_abonos = 0
valor_minimo = 0
maior_valor = 0
salario = int(input("Digite o salario (0 para sair): "))
while salario != 0:
    funcionarios = funcionarios + [salario]
    print(funcionarios)
    salario = int(input("Digite o salario (0 para sair): "))
    

abono_funcionarios = [0] * len(funcionarios)
i = 0
for salario in funcionarios:
    abono = salario * 0.2
    if(abono <= 100):
        abono_funcionarios[i] = 100
        valor_minimo = valor_minimo + 1
    else:
        abono_funcionarios[i] = abono
    total_abonos = total_abonos + abono_funcionarios[i]
    if(abono_funcionarios[i] > maior_valor):
        maior_valor = abono_funcionarios[i]
    i = i + 1
    print(abono_funcionarios)
i = 0
print("Salario     - Abono")
for salario in funcionarios:
    print("R$ %8.2f - R$ %5.2f" %(salario, abono_funcionarios[i]))
    i = i + 1

print("Foram processados %d funcionarios" % len(funcionarios))
print("Total gasto com abonos: R$ %.2f" % total_abonos)
print("Valor minimo pago a %d funcionarios" % valor_minimo)
print("Maior valor de abono pago: R$ %.2f" % maior_valor)
