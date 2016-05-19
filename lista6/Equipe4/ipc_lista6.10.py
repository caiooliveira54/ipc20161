def mdc(numero1, numero2):
    if numero1 == 0:
        return numero2
    if numero2 == 0:
        return numero1
    else:
        return mdc(numero2, numero1%numero2)

print ("Programa que calcula o MDC de dois numeros")
numero1 = int(input("Qual o primeiro numero? "))
numero2 = int(input("Qual o segundo numero? "))
print ("\nMMD(%d, %d) ="%(numero1, numero2), mdc(numero1, numero2))
