#Introdução a Programação de Computadores
#Professor: Jucimar JR
#EQUIPE 5
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#Luiz Alexandre Oliveira de Souza - 1615310057

def fat (n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return n * fat(n-1)
num = int(input("Difite um numero: !"))
resultado = fat(num)
print ("O fatorial de %d corresponde a %d" % (num,resultado))
