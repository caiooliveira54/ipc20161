#Introducao a programacao de computadores
#Professor: Jucimar Junior
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Nahan Trindade Passos - 1615310021

def criar_cadastros(clientes, colunas):
    cadastros = [["CLIENTE", "CONTA", "SALDO"]]
    for i in range(clientes):
        cliente = []
        for j in range(3):
            if j == 0:
                nome = str(input("\nQual seu nome? "))
                cliente.append(nome)
            if j == 1:
                conta = int(input("Qual o numero da conta corrente? "))
                cliente.append(conta)
            if j == 2:
                saldo = int(input("Qual o saldo total da conta? "))
                cliente.append(saldo)
        cadastros.append(cliente)
    return cadastros

def imprimir(cadastros):
    for i in range(len(cadastros)):
        print (cadastros[i])

def atualizar_contas(matriz):
    operaçoes = int(input("Quantas operaçoes foram realizadas? "))
    for a in range(operaçoes):
        codigo = int(input("\nQual sua conta corrente? "))
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == codigo:
                    print ("Seja bem vindo", matriz[i][j-1],"seu saldo e de R$",matriz[i][j+1])
                    operaçao = str(input("Operaçao de credito ou debito (c/d)?"))
                    if operaçao == "c" or operaçao == "C":
                        valor = int(input("Qual o valor desejado para credito? "))
                        matriz[i][j+1] = matriz[i][j+1] - valor
                        break
                    if operaçao == "d" or operaçao == "D":
                        valor = int(input("Qual o valor desejado para debito? "))
                        matriz[i][j+1] = matriz[i][j+1] - valor
                        break

print ("Cadastro dos clientes de um banco v1.0")
clientes = int(input("Quantos usuarios tem o banco? "))
colunas = 3
cadastros = criar_cadastros(clientes, colunas)
print ("\nTabela com cadastros:")
imprimir(cadastros)
print ("\nAtualizaçoes nas contas")
atualizar_contas(cadastros)
print ("\nTabela atualizada:")
imprimir(cadastros)
