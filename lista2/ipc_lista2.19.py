#
#Igor Menezes Sales Vieira 1615310007 
#Kid Mendes de Oliveira Neto 1615310011
#Victor Rafael da Silva e Silva 1615310025
#Josue Vasques Catachunga 1615310054
#

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
