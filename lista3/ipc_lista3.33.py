#Introduçao a programaçao de computadores
#Professor: Jucimar Junior
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
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

