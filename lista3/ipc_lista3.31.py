#Introduçao a programaçao de computadores
#Professor: Jucimar Junior
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#

while (True):
    cont = 0
    prod = 0
    total = 0
    print ("Lojas Tabajara")
    while (True):
        prod = prod + 1
        produtos = float(input("Insira o valor do produto %d: R$ "%(prod)))
        if (produtos == 0):
            break
        total = total + produtos
    print ("Total: R$ %.2f"%total)
    valor_pago = float(input("Insira o valor pago pelo cliente: R$ "))
    troco = valor_pago - total
    print ("Troco: R$ %.2f"%(troco))
    print ("------------------------------------------------------------------------")
