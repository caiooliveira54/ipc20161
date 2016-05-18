#Introdução a Programação de Computadores
#Professor: Jucimar JR
#EQUIPE 5
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#Luiz Alexandre Oliveira de Souza - 1615310057

def soma(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + soma(n-1)

print("Digite o número que você deseja somar: ")
n = int(input("(Vamos somá-lo de 1, até o número que você digitou): "))
print(soma(n))
