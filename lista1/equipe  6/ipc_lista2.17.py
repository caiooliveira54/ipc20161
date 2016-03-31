#
#Igor Menezes Sales Vieira 1615310007 
#Kid Mendes de Oliveira Neto 1615310011
#Victor Rafael da Silva e Silva 1615310025
#Josue Vasques Catachunga 1615310054
#

ano = input("Digite um ano:\n")

if(ano%4==0 and ano%100!=0 or ano%400==0):
    print("Ano Bissexto")
else:
    print("Nao e ano bissexto")
