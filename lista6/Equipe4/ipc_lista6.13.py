def imprimir_decrescente(numero):
    if numero == 0:
        return 0
    else:
        return str(numero) + " " + str(imprimir_decrescente(numero-1))

print ("Programa que imprime os numeros de N ate 0")
numero = int(input("Qual o valor de N? "))
print ("\nResultado:", imprimir_decrescente(numero))

