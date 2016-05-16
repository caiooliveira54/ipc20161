#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 5
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#

def criar_contas(clientes):
    cadastros = []
    for i in range(clientes):
        clientes = []
        for j in range(3):
            if j == 0:
                usuario = input("\nNome do cliente: ")
                clientes.append(usuario)
            if j == 1:
                conta = i+1
                print("O numero da sua conta corrente é %d" %(conta))
                clientes.append(conta)
            if j == 2:
                saldo = float(input("Qual o saldo total da conta: R$"))
                clientes.append(saldo)
        cadastros.append(clientes)
    return cadastros

def imprimir(cadastros):
    print ("CLIENTE-CONTA-SALDO")
    for i in range(len(cadastros)):
        print (cadastros[i])

def operacao(matriz):
    operaçoes = int(input("\nOperacoes!!!\nQuantas operaçoes voce deseja realisar: "))
    for o in range(operaçoes):
        conta = int(input("\nNumero da sua conta correnta: "))
        for i in range(len(matriz)):
            if matriz[i][1] == conta:
                print ("\nOla %s!!!\nSeu saldo atual é de R$ %5.2f" %(matriz[i][0],matriz[i][2]))
                atualizacao = input("\nQual operacao voce deseja realizar Credito(c) ou Debito(d): ")
                if atualizacao == "c" or atualizacao == "C":
                    valor = float(input("\nQuanto vc deseja de credito: R$"))
                    matriz[i][2] = matriz[i][2] + valor
                if atualizacao == "d" or atualizacao == "D":
                    valor = float(input("\nQuanto deve ser debitado: R$"))
                    matriz[i][2] = matriz[i][2] - valor
                    


logins = int(input("Cadastrar clientes do banco\nQuantos usuarios tem o banco: "))
cadastros = criar_contas(logins)
print ("\nCadastros realizados!!!")
imprimir(cadastros)
operacao(cadastros)
print ("\nOperacoes realizadas!!!")
imprimir(cadastros)
