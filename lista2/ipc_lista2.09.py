#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 2
#
#Ana Beatriz Frota  - 1615310027 
#Kylciane Cristiny Lopes Freitas - 1615310052
#Frankilin Yuri Gonçaves dos santos - 1615310033
#Lucas Ferreira Soares - 1615310014
#Luiz Gustavo Rocha Melo - 1615310015
#Nahan Trindade Passos - 1615310021
#Samuel Silva França - 1615310049
#Luiz Alexandre Oliveira de Souza - 1615310057
#



cont = 1 #contador
numero = 1 #variável 

while (cont <= 49): #enquanto o contador for menor/igual 49:
    numero= numero + 1 #numero igual ao seu sucessor
    cont = cont + 1 #contador + 1
    if (numero%2 !=0): # se o resto da divisão do numero por 2 for diferente de  zero (impar)
        print(numero)
