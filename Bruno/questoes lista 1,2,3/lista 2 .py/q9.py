num1=int(input("Informe o primeiro numero: "))
num2=int(input("Informe o segundo numero: "))
num3=int(input("Informe o terceiro numero: "))
maior=0
menor=0
meio=0
if (num1>=num2 and num1>=num3):
    maior = num1
    if(num2>=num3):
        menor = num3
        meio = num2
    else:
        menor = num2
        meio = num3

if (num2>=num1 and num2>=num3):
    maior = num2
    if(num1>=num3):
        menor = num3
        meio = num1
    else:
        menor = num1
        meio = num3     

if (num3>=num2 and num3>=num1):
    maior = num3
    if(num2>=num1):
        menor = num1
        meio = num2
    else:
        menor = num2
        meio = num1

print(maior, meio, menor)

   
     
