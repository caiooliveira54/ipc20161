#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 2
#
#Ana Beatriz Frota  - 1615310027 
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Gonçaves dos Santos - 1615310033
#Lucas Ferreira Soares - 1615310014
#Luiz Gustavo Rocha Melo - 1615310015
#Nahan Trindade Passos - 1615310021
#Samuel Silva França - 1615310049
#Luiz Alexandre Oliveira de Souza - 1615310057

numero = int(input("Digite um numero menor que 1000:\n"))
numerostr = str(numero)
quantidade_numero = len(numerostr)

if(quantidade_numero == 3):
    centenas = numerostr[0:1]
    dezenas = numerostr[1:2]
    unidade = numerostr[2:3]
    print(numerostr+"= "+centenas+" centenas ,"+dezenas+" dezenas e "+unidade+" unidades")
if(quantidade_numero == 2):
    dezenas = numerostr[0:1]
    unidade = numerostr[1:2]
    print(numerostr+"= "+dezenas+" dezenas e "+unidade+" unidades")
if(quantidade_numero == 1):
    unidade = numerostr[0:1]
    print(numerostr+"= "+unidade+" unidades")