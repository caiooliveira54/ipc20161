"""
#lista de repetição

#Antonio Rodrigues de Souza Neto --- matrícula ----1615310028
#Gabriel Machado Moreira --- matrícula ----1615310034
#Luiz Gustavo de Rocha Melo --- matrícula ---- 1615310015
#Lucas Ferreira Soares --- 1615310014
#Calebe Roberto Chaves da Silva Rebello --- matrícula---1615310043

"""
entrada = int(input("Digite um número positivo inteiro: "))

primo = 1
contador = 0

entrada1 = entrada/2

while primo <= entrada:
    if entrada % primo==0:
        primo = primo+1
        contador = contador+1
    if primo >= entrada1:
        primo = entrada
        primo = primo + 1
        contador = contador + 1
    else:
        primo = primo + 1
if contador==2:
    print("O número requisitado é primo!")
else:
    print("O número requisitado não é primo!")
