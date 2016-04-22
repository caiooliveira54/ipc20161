#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 4
#
#Bruno de Oliveira Freire - 1615310030
#Igor Menezes Sales Vieira - 1615310007
#Matheus Mota de Souza - 1615310016
#Nadine da Cunha Brito - 1615310040
#Nickso Patrick Façanha Calheiros - 1615310059
#Thiago Santos Borges - 1615310023
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
