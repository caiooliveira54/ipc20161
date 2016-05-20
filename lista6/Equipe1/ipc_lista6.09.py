#Introdução a Programação de Computadores
#Professor: Jucimar JR
#EQUIPE 5
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#Luiz Alexandre Oliveira de Souza - 1615310057

def somar(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n + soma(n-1)

numero = int(input("Digite o número que você deseja somar!\nVamos somá-lo de 1, até o número que você digitou: "))
resultado = somar(numero) 
print(resultado)
