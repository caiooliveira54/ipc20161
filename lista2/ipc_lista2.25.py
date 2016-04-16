#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 2
#
#Ana Beatriz Frota  - 1615310027 
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Gonçaves dos Santos - 1615310033
#Lucas Ferreira Soares - 1615310014
#Luiz Gustavo Rocha Melo - 1615310015
#Nahan Trindade Passos - 1615310021
#Samuel Silva França - 1615310049
#Luiz Alexandre Oliveira de Souza - 1615310057
#Ariel Guilherme Rocha Capistrano - 1615310029

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
