#
#Igor Menezes Sales Vieira 1615310007 
#Kid Mendes de Oliveira Neto 1615310011
#Victor Rafael da Silva e Silva 1615310025
#Josue Vasques Catachunga 1615310054
#

print("Responda as perguntas para (1) se sim ou (0) se nao")
pergunta1 = int(input("Telefonou para a vitima?\n"))
pergunta2 = int(input("Esteve no local do crime?\n"))
pergunta3 = int(input("Mora perto da vitima?\n"))
pergunta4 = int(input("Devia para a vitima?\n"))
pergunta5 = int(input("Ja trabalhou para a vitima?\n"))

soma = (pergunta1+pergunta2+pergunta3+pergunta4+pergunta5)

if(soma == 2):
    print("Suspeita")
if(soma == 3 or soma == 4):
    print("Cumplice")
if(soma == 5):
    print("Assassino")
elif(soma == 1 or soma == 0):
    print("Inocente")
