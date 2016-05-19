def potencia(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if base == 0:
        return 0
    else:
        return base * potencia(base, exp-1)

print ("Calcular potencia")
base = int(input("Qual o numero que deseja-se calcular a potencia? "))
exp = int(input("Qual o expoente que deseja-se elevar %d? "%(base)))
resultado = potencia(base, exp)
print ("\n%d^%d ="%(base, exp), resultado)
