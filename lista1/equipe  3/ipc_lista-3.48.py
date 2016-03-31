#
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#
numero = int(input("Digite um numero:"))
aux = numero
reverso = 0

while aux != 0:
    reverso = reverso * 10 + aux % 10
    aux = aux // 10

print("O reverso de numero %d \ne %d"%(numero,reverso))

