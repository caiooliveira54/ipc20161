#
#Programa Lista 4, questão 4;
#Felipe Henrique Bastos Costa - 1615310032;
#
texto = raw_input("Informe uma palavra ou frase de 10 caracteres, espaços incluidos:\n")
cont = 0
v = 10
j = v
soma = 0
lista = []

while(cont < v):
    j-=1
    if(texto[cont] == "a" or texto[cont] == "e" or texto[cont] == "i" or texto[cont] == "o" or texto[cont] == "u" or texto[cont] == " "):
        soma = soma
    else:
        soma+=1
        x = texto[cont]
        lista.append(x)
    cont+=1
print("exitem %d consoantes, sendo elas as seguintes:\n%s"%(soma,lista))