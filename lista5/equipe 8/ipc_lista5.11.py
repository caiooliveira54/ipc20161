#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Matheus Palheta Barbosa - 1615310019
#Any Mendes Carvalho - 1615310044
#Victor Rafael da Silva e Silva - 1615310025
#

from matriz import*

contas_clientes = []

def cadastrar_clientes():
    cadastrar = input("Cadastrar Cliente? (S/N): ")
    while(cadastrar != "S" and cadastrar != "N" and cadastrar != "s" and cadastrar != "n"):
        cadastrar = input("Opcao invalida. Cadastrar Cliente? (S/N): ")
        
    numero_conta = 0
    while(cadastrar == "S" or cadastrar == "s" ):
        print("Numero da conta: ", numero_conta)
        numero_conta += 1
        saldo = float(input("Digite o saldo da conta: "))
        contas_clientes.append(saldo)
        print()
        
        cadastrar = input("Cadastrar Cliente? (S/N): ")
        while(cadastrar != "S" and cadastrar != "N" and cadastrar != "s" and cadastrar != "n"):
            cadastrar = input("Opcao invalida. Cadastrar Cliente? (S/N): ")    

def cadastrar_operacoes(operacoes):
    for i in range(operacoes):
        print()
        numero_conta = int(input("Digite o numero da conta: "))
        while(numero_conta >= len(contas_clientes)):
            numero_conta = int(input("Conta invalida. Digite o numero da conta: "))
        operacao = input("Digite a operacao (C/D): ")
        while(operacao != "C" and operacao != "c" and operacao != "D" and operacao != "d"):
            operacao = input("operacao invalida. Digite a operacao (C/D): ")
        if(operacao == "C" or operacao == "c"):
            contas_clientes[numero_conta] += float(input("Digite o valor da operacao: "))
        elif(operacao == "D" or operacao == "d"):
            contas_clientes[numero_conta] -= float(input("Digite o valor da operacao: "))    
    

cadastrar_clientes()
print()       
operacoes = int(input("Digite o numero de operacoes: "))
cadastrar_operacoes(operacoes)        
for i in range(len(contas_clientes)):
    print("Numero conta %d saldo:%.2f" %(i, contas_clientes[i]))
        