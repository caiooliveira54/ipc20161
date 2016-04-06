nota1 = float(input(" digite o número 1 "))
nota2 = float(input(" digite o número 2 "))
nota3 = float(input(" digite o número 3 "))
acumulador = 0
if( nota1>=nota2 and nota1>=nota3 ):
    acumulador=nota1
if( nota2>=nota1 and nota2>=nota3 ):
    acumulador=nota2
if( nota3>=nota1 and nota3>=nota2):
    acumulador=nota3

print(acumulador)
