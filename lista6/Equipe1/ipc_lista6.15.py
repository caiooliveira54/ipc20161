#Introdução a Programação de Computadores
#Professor: Jucimar JR
#EQUIPE 1
#Ariel Guilherme Rocha Capistrano - 1615310029
#Luiz Alexandre Oliveira de Souza - 1615310057
#Nickso Patrick Façanha Calheiros - 1615310059

def recursiva_decrescentepar(numero):
    if numero == 0:
        return 0
    else:
        return  str(numero) + " " + str(recursiva_decrescentepar(numero - 2))
    
n = int(input("digite o numero: "))
print(recursiva_decrescentepar(n))
