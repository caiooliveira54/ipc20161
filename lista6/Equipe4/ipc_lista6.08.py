def MDC(numero1,  numero2):
    if numero2 == 0:
        return numero1
    if numero1 > numero2:
        return MDC(numero2, numero1%numero2)
    if numero2 > numero1:
        return MDC(numero1, numero2%numero1)
    
print ("Programa que calcula o MDC de dois números")
num1 = int(input("Qual o primeiro número? "))
num2 = int(input("Qual o segundo número? "))
print ("\nO MDC(%d,%d) ="%(num1, num2), MDC(num1,num2))
