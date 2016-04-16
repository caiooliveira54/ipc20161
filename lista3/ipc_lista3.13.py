#Introdução a programação de computadores;
#Professor: Jucimar Junior
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#Caio de Oliveira Martins - 1615310031
#Antonio Rodrigues de Souza Neto - 1615310028
#Calebe Roberto Chaves da Silva Rebello - 1615310043

base=int(input("Digite o valor da base:"))
expoente=int(input("Digite o valor do expoente:"))

cont=0
produto=1
while cont < expoente:
    produto=produto*base
    cont=cont+1

print(base, "elevado a", expoente, "=", produto)    
