#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 3
#
#Antonio Rodrigues de Souza Neto - 1615310028
#Caio de Oliveira Martins - 1615310031
#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#

num = int(input("Calcular a tabuada do número: "))
multiplicador = 1

tabuada = (num * multiplicador)

while (multiplicador < 10):
    print(num,"X",multiplicador,"=",tabuada)
    multiplicador = multiplicador + 1
    tabuada = (num * multiplicador)    

print(num,"X",multiplicador,"=",tabuada)
