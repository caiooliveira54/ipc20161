def par_decrescente(numero):
    if numero == 0:
        return 0
    if numero % 2 == 0:
        return str(numero) + " " + str(par_decrescente(numero-2))

print ("Programa que imprime numeros pares de 0 ate N")
numero = int(input("Qual o valor de N? "))
print ("\nResultado:", par_decrescente(numero))
