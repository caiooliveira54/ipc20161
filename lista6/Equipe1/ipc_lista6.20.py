def fatorial_exponencial(numero):
    if numero ==  1:
        return 1
    else:
        return numero ** fatorial_exponencial(numero - 1)

n = int(input("digite um numero: "))
print(fatorial_exponencial(n))
