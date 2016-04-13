#professor Jucimar junior
#Ana Jessye 1615310046, 
#Franklin Yuri 1615310033,
#Kylciane Freitas 1615310032 
#Madson Lemos 1615310037
#IPC_Lista3.7

valida = 0

while (valida ==0 ):
    num1 = float(input("Informe o primeiro numero: \n"))
    num2 = float(input("Informe o segundo numero: \n"))
    num3 = float(input("Informe o terceiro numero: \n"))
    num4 = float(input("Informe o quarto numero: \n"))
    num5 = float(input("Informe o quinto numero: \n"))
    
    if(num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5):
        print(num1, " o maior numero")
    
    if(num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5):
        print(num2, "é o maior numero")
    
    if(num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5):
        print(num3, "é o maior numero") 
        
    if(num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5):
        print(num1, "é o maior numero")   
        
    if(num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4):
        print(num1, "é o maior numero") 
        
    valida = int(input("Quer fazer de novo? 0-Sim - 1-Nao: \n"))
    
