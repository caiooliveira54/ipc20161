def multiplicar(numero, mult):
    if mult == -1:
        return -numero
    if mult < 0:
        return numero - multiplicar(numero, mult+1)
    if mult == 1:
        return numero
    if mult == 0:
        return 0
    if numero == 0:
        return 0
    if numero > 0:
        return numero + multiplicar(numero, mult-1)

print ("Mutiplicador de numeros inteiros")
numero = int(input("Qual o numero a ser multiplicado? "))
mult = int(input("Quantas vezes esse numero deve ser multiplicado? "))
produto = multiplicar(numero, mult)
print ("\n%dx%d ="%(numero, mult), produto)
