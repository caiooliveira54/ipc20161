def fatorial_duplo(numero):
    if numero == 1:
        return 1
    else:
        return numero * fatorial_duplo(numero - 2)

n = int(input("digite o numero: "))
print(fatorial_duplo(n))
