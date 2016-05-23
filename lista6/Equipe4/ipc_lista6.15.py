def par_decrescente(numero):
    if numero == 0:
        return 0
    if numero % 2 == 0:
        return str(numero) + " " + str(par_decrescente(numero-2))

print ("Programa que imprime numeros pares de N ate 0")
numero = int(input("Qual o valor de N? "))
print ("\nResultado:", par_decrescente(numero))
