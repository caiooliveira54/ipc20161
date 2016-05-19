def par_crescente(numero):
    if numero == 0:
        return 0
    if numero % 2 == 0:
        return str(par_crescente(numero-2)) + " " + str(numero)

print ("Programa que imprime numeros pares de 0 ate N")
numero = int(input("Qual o valor de N? "))
print ("\nResultado:", par_crescente(numero))
