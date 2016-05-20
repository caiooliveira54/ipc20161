#Introdução a Programação de Computadores
#Professor: Jucimar JR
#EQUIPE 1
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#Luiz Alexandre Oliveira de Souza - 1615310057

def fib (n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 1:
        return fib(n - 1) + fib(n - 2)
num = int(input("Aposição na lista de Fibonacci: "))
resultado = fib(num)

print ("O numero na posição %d é %d" % (num,resultado))
