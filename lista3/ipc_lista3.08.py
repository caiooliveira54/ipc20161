#Introdução a programação de computadores;
#Professor: Jucimar Junior
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#Caio de Oliveira Martins - 1615310031
#Antonio Rodrigues de Souza Neto - 1615310028
#Calebe Roberto Chaves da Silva Rebello - 1615310043

valida = 0

while (valida ==0 ):
    num1 = float(input("Informe o primeiro numero: \n"))
    num2 = float(input("Informe o segundo numero: \n"))
    num3 = float(input("Informe o terceiro numero: \n"))
    num4 = float(input("Informe o quarto numero: \n"))
    num5 = float(input("Informe o quinto numero: \n"))
    
    
    soma = (num1+num2+num3+num4+num5)
    media = (soma/5)
    
    print ("Soma: ",soma)
    print ("Media",media)
    valida = int(input("Quer tentar de novo? 0-Sim - 1-Nao: \n"))
