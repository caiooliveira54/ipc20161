#Introdução a Programação de Computadores
#Professor: Jucimar JR
#EQUIPE 1
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#Luiz Alexandre Oliveira de Souza - 1615310057

def somar_n (n):
    if n == 1:
        return 1
    else:
        return n + somar_n(n-1)

numero = int(input("Digite um numero: "))
print ("A soma dos numeros de 1 a %d é %d" %(numero,somar_n(numero)))
