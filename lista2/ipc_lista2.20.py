#
#Igor Menezes Sales Vieira 1615310007 
#Kid Mendes de Oliveira Neto 1615310011
#Victor Rafael da Silva e Silva 1615310025
#Josue Vasques Catachunga 1615310054
#

nota1 = float(input("Primeira nota parcial:\n"))
nota2 = float(input("Segunda nota parcial:\n"))
nota3 = float(input("Terceira nota parcial:\n"))

media = (nota1+nota2+nota3)/3

if(10>media >= 7):
    print("Aprovado! %.2f"%media)
elif(media == 10):
    print("Aprovado com distincao!",media)
else:
    print("Reprovado %.2f"%media)
