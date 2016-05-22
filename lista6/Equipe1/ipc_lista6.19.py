def hiper_fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero ** numero * hiper_fatorial(numero - 1)

n = int(input("digite um numero: "))
print(hiper_fatorial(n))
