#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 2
#
#Ana Beatriz Frota  - 1615310027 
#Ariel Guilherme Rocha Capistrano - 1615310029
#Frankilin Yuri Gonçaves dos santos - 1615310033
#Kylciane Cristiny Lopes Freitas - 1615310052
#Lucas Ferreira Soares - 1615310014
#Luiz Alexandre Oliveira de Souza - 1615310057
#Luiz Gustavo Rocha Melo - 1615310015
#Nahan Trindade Passos - 1615310021
#Samuel Silva França - 1615310049
#

numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))

operacao = input("Escolha uma operacao: (+)-Adicao;(-)-Subtracao;(*)-Multiplicacao;(/)-Divisao\n")

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
