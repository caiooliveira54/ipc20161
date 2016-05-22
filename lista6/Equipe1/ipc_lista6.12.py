def recursiva_crescente(numero):
    if numero == 0:
        return 0
    else:
        return  str(recursiva_crescente(numero - 1)) + " " + str(numero)
    
n = int(input("digite o numero: "))
print (recursiva_crescente(n))
