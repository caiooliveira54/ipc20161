"""
#lista de repetição

#Antonio Rodrigues de Souza Neto --- matrícula ----1615310028
#Gabriel Machado Moreira --- matrícula ----1615310034
#Luiz Gustavo de Rocha Melo --- matrícula ---- 1615310015
#Lucas Ferreira Soares --- 1615310014
#Calebe Roberto Chaves da Silva Rebello --- matrícula---1615310043

"""

N = int(input("Digite um número inteiro: "))

primo = 1
contador = 0
N1 = N/2

while primo <= N:
    if (N % primo==0):
        primo = primo + 1
        contador = contador + 1
    if (primo >= N1):
        primo = N
        primo = primo + 1
        contador = contador + 1
    else:
        primo = primo + 1
if contador==2:
    print("O número de divisões foi",contador)
else:
    print("O número de divisões foi",contador)
