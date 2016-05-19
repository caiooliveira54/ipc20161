def imprimir_crescente(numero):
    if numero == 0:
        return 0
    else:
        return str(imprimir_crescente(numero - 1)) + " " + str(numero)

print ("Programa que imprime numeros de 0 ate N")    
numero = int(input("Qual o valor de N? "))
print ("\nResultado:", imprimir_crescente(numero))

