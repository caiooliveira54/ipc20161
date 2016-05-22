def recursiva_decrescentepar(numero):
    if numero == 0:
        return 0
    else:
        return  str(numero) + " " + str(recursiva_decrescentepar(numero - 2))
    
n = int(input("digite o numero: "))
print(recursiva_decrescentepar(n))
