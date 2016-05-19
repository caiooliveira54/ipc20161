def inverter(n):
    if len(str(n)) == 1:
        return n
    else:
        return str(n % 10) + str(inverter(n//10))

print ("Inversor de numeros")
numero = int(input("Qual o numero que deseja-se inverter? "))
inverso = inverter(numero)
print ("O inverso de %d é"%(numero), inverso)
