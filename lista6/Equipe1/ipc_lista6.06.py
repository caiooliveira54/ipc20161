#Introdução a Programação de Computadores
#Professor: Jucimar JR
#EQUIPE 1
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#Luiz Alexandre Oliveira de Souza - 1615310057

def potenciacao(k,n):
    if n == 0:
        return 1
    if n == 1:
        return k
    else:
        return k * potenciacao(k,n-1)

base = int(input("Digite o numero da base da potenciação: "))
expoente = int(input("Digite o expoente da potenciação: "))
resultado = potenciacao(base,expoente)
print ("%d elevado a potencia %d é igual %d" %(base,expoente,resultado))
