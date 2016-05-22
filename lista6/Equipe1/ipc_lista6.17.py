def fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

def fatorial_qua(numero):
    if numero == 1:
        return 2
    else:
        return (fatorial(2*numero)/fatorial(n))

n = int(input("digite o numero: "))
print(fatorial_qua(n))
