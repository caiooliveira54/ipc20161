#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 4
#
#Bruno de Oliveira Freire - 1615310030
#Igor Menezes Sales Vieira - 1615310007
#Matheus Mota de Souza - 1615310016
#Nadine da Cunha Brito - 1615310040
#Nickso Patrick Façanha Calheiros - 1615310059
#Thiago Santos Borges - 1615310023
#

quantidade = int(input("Insira a quantidade de temperaturas a serem usadas: "))
cont = 0
soma = 0
menor = 1000000
maior = 0

while (cont<quantidade):
    temperatura = float(input("Insira a temperatura: "))
    if temperatura>maior:
        maior = temperatura
    if temperatura<menor:
        menor = temperatura
    cont +=1
    soma = soma + temperatura
    media = soma / quantidade
print ("A maior temperatura e %d \nA menor temperatura e %d \nA media das temperaturas e %.1d"%(maior, menor, media))
