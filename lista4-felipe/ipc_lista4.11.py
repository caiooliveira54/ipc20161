#
#Programa Lista 4, questão 11;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista1 = [] # Primeiro vetor
lista2 = [] # Segundo vetor
lista3 = [] # Terceiro vetor
lista4 = [] # Quarto vetor que receberá os valores dos vetores acima de forma alternada
v1 = 10 # Limite para cada vetor
cont1 = 0 
cont2 = 1

while(cont1 < v1): # Enquanto verdade solicitará números para serem adicionados ao vetor 1, 2 e 3 e serão acrescidos de forma alternada no vetor 4
    x1 = raw_input("Informe o %dº elemento a ser colocado na 1º lista:\n"%cont2)
    x2 = raw_input("Informe o %dº elemento a ser colocado na 2º lista:\n"%cont2)
    x3 = raw_input("Informe o %dº elemento a ser colocado na 3º lista:\n"%cont2)
    lista1.append(x1)
    lista2.append(x2)
    lista3.append(x3)
    lista4.append(x1)
    lista4.append(x2)
    lista4.append(x3)
    cont1+=1
    cont2+=1

print("A uniao das listas de forma alternada e:\n%s"%lista4) # Resultado do vetor 4
