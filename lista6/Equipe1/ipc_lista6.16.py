#Introdução a Programação de Computadores
#Professor: Jucimar JR
#EQUIPE 1
#Ariel Guilherme Rocha Capistrano - 1615310029
#Luiz Alexandre Oliveira de Souza - 1615310057
#Nickso Patrick Façanha Calheiros - 1615310059

def fatorial_duplo(numero):
    if numero == 1:
        return 1
    else:
        return numero * fatorial_duplo(numero - 2)

n = int(input("digite o numero: "))
print(fatorial_duplo(n))
