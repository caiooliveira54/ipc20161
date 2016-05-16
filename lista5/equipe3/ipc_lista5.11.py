#Coding: utf-8
#Introducao a programacao de computadores
#Professor: Jucimar Junior
#samuel silva de frança - 1615310049
#bruno de oliveira freire - 1615310030
#Felipe Henrique Bastos Costa - 1615310032

def fazer_cadastro(clientes):
    cadastros = [["Cliente","Conta","Saldo"]]
    for i in range(clientes):
        dados = []
        for j in range(3):
            if j == 0:
                nome = str(input("Informe o nome do %dº cliente: "%(i+1)))
                dados.append(nome)
            if j == 1:
                num_cadastro = int(input("Informe o número da conta: "))
                dados.append(num_cadastro)
            if j == 2:
                saldo = float(input("Informe o saldo original da conta: "))
                dados.append(saldo)
        cadastros.append(dados)
    return cadastros

def atualizar_contas(matriz):
    num = int(input("Informe o número de operações feitas no dia: "))
    for n in range(num):
        conta = int(input("Informe o número da sua conta: "))
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == conta:
                    print("Seja bem vindo, %s,"%matriz[i][0] + "seu saldo atual e de R$ %.2f."%matriz[i][2])
                    tipo = str(input("A operação sera feita usando crédito ou debito (c ou d)?\n"))
                    if tipo == "c" or tipo == "crédito" or tipo == "credito":
                        valor = float(input("Informe o valor da operação com crédito: "))
                        matriz[i][2] -= valor
                    if tipo == "d" or tipo == "débito" or tipo == "debito":
                        valor = float(input("Informe o valor da operação com débito: "))
                        matriz[i][2] -= valor
        mostrar_contas(matriz)
                    
def mostrar_contas(cadastros):
    for i in range(len(cadastros)):
        if i == 0:
            print ["%s"%cadastros[i][0],"%s"%cadastros[i][1],"%s"%cadastros[i][2]]
        else:
            print ["%s"%cadastros[i][0],"%d"%cadastros[i][1],"R$ %.2f"%cadastros[i][2]]
qtd_clientes = int(input("Informe o numero de clientes do banco:\n"))
banco_de_dados = fazer_cadastro(qtd_clientes)
mostrar_contas(banco_de_dados)
atualizacao = atualizar_contas(banco_de_dados)
