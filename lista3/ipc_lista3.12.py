"""
#lista de repetição

#Antonio Rodrigues de Souza Neto --- matrícula ----1615310028
#Gabriel Machado Moreira --- matrícula ----1615310034
#Luiz Gustavo de Rocha Melo --- matrícula ---- 1615310015
#Lucas Ferreira Soares --- 1615310014
#Calebe Roberto Chaves da Silva Rebello --- matrícula---1615310043

"""

num = int(input("Calcular a tabuada do número: "))
multiplicador = 1

tabuada = (num * multiplicador)

while (multiplicador < 10):
    print(num,"X",multiplicador,"=",tabuada)
    multiplicador = multiplicador + 1
    tabuada = (num * multiplicador)    

print(num,"X",multiplicador,"=",tabuada)
