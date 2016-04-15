#
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#

while True:
    numero = int(input("Insira um numero: "))
    if (numero==1):
        print ("Nao e primo")
    elif (numero/1==numero):
        if (numero/numero==1):
            if (numero%2==0) or (numero%3==0) or (numero%4==0) or (numero%5==0) or (numero%6==0) or (numero%7==0) or (numero%8==0) or (numero%9==0):
                print ("Nao e primo")
            else:
                print ("E primo")
