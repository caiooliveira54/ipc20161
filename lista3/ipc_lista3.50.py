#
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#
N  = int(input("N:"))
cont = 1
H = 0
while cont < (N+1):
    print("1/",cont)
    H = H + (1/cont)
    cont = cont + 1
print("O resultado da serie ",H)
