#Introdução a Programação de Computadores
#Professor: Jucimar JR
#EQUIPE 1
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#Luiz Alexandre Oliveira de Souza - 1615310057

def inverter (n):
    ac = 0
    if len (str(n)) == 1:
        return n
    else:
        return str(n % 10) + str(inverter(n // 10))
        

num = int(input("Digite um numero: "))
print(inverter(num))
