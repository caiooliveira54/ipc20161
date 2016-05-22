def recursiva_crescentepar(numero):
    if numero == 0:
        return  0
    else:
        return  str(recursiva_crescentepar(numero - 2)) + " " + str(numero)
    
n = int(input("digite o numero: "))
print (recursiva_crescentepar(n))
