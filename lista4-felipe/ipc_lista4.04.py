#
#Programa Lista 4, questão 4;
#Felipe Henrique Bastos Costa - 1615310032;
#
texto = raw_input("Informe uma palavra ou frase de 10 caracteres, espaços incluidos:\n") # Solicita ao usuário o texto de 10 caracteres
cont = 0 # Contador para ser incrementado e funcionará como índice da string
v = 10 # Limitador do contador
soma = 0 # Acumulador para quantidade de consoantes
lista = [] # Vetor que receberá todas as consoantes

while(cont < v):
    if(texto[cont] == "a" or texto[cont] == "e" or texto[cont] == "i" or texto[cont] == "o" or texto[cont] == "u" or texto[cont] == " "):
        soma = soma # Acima temos uma condição para ser vogal e ao lado temos a soma sendo ela mesma, pois não haverá consoante nessa condição
    else: # Caso não caia na condição acima, será acrescido a soma mais um e a consoante será adicionada à lista
        soma+=1
        x = texto[cont]
        lista.append(x)
    cont+=1 # Incrementando o contador para evitar loop
print("exitem %d consoantes, sendo elas as seguintes:\n%s"%(soma,lista)) # Impressão da lista com consoantes e a quantidade delas
