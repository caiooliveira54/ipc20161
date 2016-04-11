lista_salario = []
lista_abono = []
cont1 = 1
cont2 = 0
cont3 = 0
cond = True

while cond:
    salario = input("Informe o salario do %dº funcionário(digite 0 para terminar o programa):\n"%cont1)
    abono = salario*0.2
    if salario == 0:
        cond = False
    elif abono <= 100:
        abono = 100
        lista_salario.append(salario)
        lista_abono.append(abono)        
        cont2 += 1
        cont3 += 1
    if abono > 100:
        lista_salario.append(salario)
        lista_abono.append(abono)
        cont3 += 1
    cont1 += 1
maior = 0
soma = 0
for i in range(cont3):
    if lista_abono[i] > maior:
        maior = lista_abono[i]
    soma = soma + lista_abono[i]
print("Projecao de gastos com abono")
print("============================")
print("Salario    -    Abono")
for i in range(cont3):
    print("R$ %.2f        %.2f"%(lista_salario[i],lista_abono[i]))
print("Foram processados %d funcionarios"%cont3)
print("Total gasto com abonos:R$ %.2f"%soma)
print("O valor minimo foi pago a %d funcionarios"%cont2)
print("O maior valor de abono pago foi:R$ %.2f"%maior)