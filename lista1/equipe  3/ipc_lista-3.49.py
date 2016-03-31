#
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#
cont = 0
n = 1
m = 1
soma = 0
limite = int(input("Digite limite:"))
while cont < limite:
    print(n,"/",m)
    soma = soma + (n/m)
    n = n + 1
    m = m +2
    cont = cont + 1
    
print("A soma da serie ",soma)
