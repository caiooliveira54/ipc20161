def recursiva_decrescente(numero):
    if numero == 0:
        return 0
    else:
        return  str(numero) + " " + str(recursiva_decrescente(numero - 1))
    
n = int(input("digite o numero: "))
print (recursiva_decrescente(n))
