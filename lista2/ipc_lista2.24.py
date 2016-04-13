#
#Igor Menezes Sales Vieira 1615310007 
#Kid Mendes de Oliveira Neto 1615310011
#Victor Rafael da Silva e Silva 1615310025
#Josue Vasques Catachunga 1615310054
#

numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))

operacao = raw_input("Escolha uma operacao: (+)-Adicao;(-)-Subtracao;(*)-Multiplicacao;(/)-Divisao\n")

if(operacao == "+"):
    adicao = (numero1+numero2)
    print("O resultado sera:",adicao)
    if(adicao%2 == 0):
        print("Numero par")
    else:
        print("Numero impar")
    if(adicao>0):
        print("Positivo")
    else:
        print("Negativo")
    if(round(adicao) != adicao):
        print("Decimal")
    else:
        print("Inteiro")
if(operacao == "-"):
    subtracao = (numero1-numero2)
    print("O resultado sera:",subtracao)
    if(subtracao%2 == 0):
        print("Numero par")
    else:
        print("Numero impar")
    if(subtracao>0):
        print("Positivo")
    else:
        print("Negativo")
    if(round(subtracao) != subtracao):
        print("Decimal")
    else:
        print("Inteiro")
if(operacao == "*"):
    multiplicacao = (numero1*numero2)
    print("O resultado sera:",multiplicacao)
    if(multiplicacao%2 == 0):
        print("Numero par")
    else:
        print("Numero impar")
    if(multiplicacao>0):
        print("Positivo")
    else:
        print("Negativo")
    if(round(multiplicacao) != multiplicacao):
        print("Decimal")
    else:
        print("Inteiro")
if(operacao == "/"):
    divisao = (numero1/numero2)
    print("O resultado sera:",divisao)
    if(divisao%2 == 0):
        print("Numero par")
    else:
        print("Numero impar")
    if(divisao>0):
        print("Positivo")
    else:
        print("Negativo")
    if(round(divisao) != divisao):
        print("Decimal")
    else:
        print("Inteiro")


