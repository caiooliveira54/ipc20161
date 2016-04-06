num1 = int(input(" me de o primeiro numero "))
num2 = int(input(" me de o segundo numero "))
num3 = int(input(" me de o terceiro numero "))
acumulador = 0
acumulador1 = 0
if(num1>=num2 and num1>=num3):
    acumulador = num1
if(num2>=num1 and num2>=num3):
    acumulador = num2
if(num3>=num1 and num3>=num2):
    acumulador = num3


if(num1<=num2 and num1<=num3):
    acumulador1 = num1
if(num2<=num1 and num2<=num3):
    acumulador1 = num2
if(num3<=num1 and num3<=num2):
    acumulador1 = num3

print(" o maior numero : " ,acumulador)
print("o menor numero : " ,acumulador1)
