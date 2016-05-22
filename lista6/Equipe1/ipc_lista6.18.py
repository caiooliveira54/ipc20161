def fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

def super_fatorial(numero):
    if  numero == 1:
        return 1
    else:
        return (numero * fatorial(numero - 1)) * super_fatorial(numero - 1)

n = int(input("digite um numero: "))
print(super_fatorial(n))
