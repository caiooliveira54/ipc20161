#Introdução a Programação de Computadores
#Professor: Jucimar JR
#EQUIPE 1
#Ariel Guilherme Rocha Capistrano - 1615310029
#Luiz Alexandre Oliveira de Souza - 1615310057
#Nickso Patrick Façanha Calheiros - 1615310059

def fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

def super_fatorial(numero):
    if  numero == 1:
        return 1
    else:
        return (numero * fatorial(numero - 1)) * super_fatorial(numero - 1)

n = int(input("digite um numero: "))
print(super_fatorial(n))
