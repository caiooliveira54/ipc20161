#
#Programa Lista 4, questão 14;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista = [] # Vetor que armazenará todas as respostas das perguntas a, b, c, d, e
cont = 0 # Contará quantas respostas foram respondidas positivamente

a = raw_input("Telefonou para a vítima?\n")    ##
b = raw_input("Esteve no local do crime?\n")    #
c = raw_input("Mora perto da vítima?\n")        # Perguntas a serem feitas para o usuário
d = raw_input("Devia para a vítima?\n")         #
e = raw_input("Já trabalhou com a vítima?\n")  ##

lista.append(a) ##
lista.append(b)  # 
lista.append(c)  # Adicionará todas as respostas ao vetor 'lista'
lista.append(d)  #
lista.append(e) ##

for i in range(5): # Verificará item a item na lista e ver quais são respondidos com sim
    if(lista[i] == "Sim" or lista[i] == "sim"):
        cont += 1 # Contará quantos sim terá
if(cont < 2):                   ## 
    print("Inocente")            #
elif(cont == 2):                 #
    print("Suspeita")            #  Condições para classificação do suspeito
elif(cont > 2 and cont < 5):     #
    print("Cumplice")            #
else:                            #
    print("Assassino")          ##
