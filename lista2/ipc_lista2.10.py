#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 2
#
#Ana Beatriz Frota  - 1615310027 
#Ariel Guilherme Rocha Capistrano - 1615310029
#Frankilin Yuri Gonçaves dos santos - 1615310033
#Kylciane Cristiny Lopes Freitas - 1615310052
#Lucas Ferreira Soares - 1615310014
#Luiz Alexandre Oliveira de Souza - 1615310057
#Luiz Gustavo Rocha Melo - 1615310015
#Nahan Trindade Passos - 1615310021
#Samuel Silva França - 1615310049
#

numero1 = int(input("Insira um numero: ")) #PEDE UM NUMERO PARA INICIAR A CONTAGEM
numero2 = int(input("Insira outro numero: ")) #PEDE UM NUMERO PARA TERMINAR A CONTAGEM

while (numero1<(numero2 - 1)): #CONDIÇÃO PARA CONTAGEM
    numero1 += 1 
    print (numero1)

while (numero2 <(numero1 - 1)):
    numero2 += 1
    print (numero2)
