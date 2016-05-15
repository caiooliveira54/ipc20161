#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Kid Mendes de Oliveira Neto - 1615310011
#Eduardo Maia Freire - 1615310003
#Igor Menezes Sales Vieira - 1615310007
#

def produzir_registros(numero_usuario):
    registro = [["Usuario", "N.Conta", "Saldo A."]]
    for n in range(numero_usuario):
        usuario = []
        for i in range(3):
            if(i == 0):
                nome_usuario = raw_input("Digite seu nome:\n ")
                usuario.append(nome_usuario)
            if(i == 1):
                numero_conta = int(input("Digite seu numero da conta:\n"))
                usuario.append(numero_conta)
            if(i == 2):
                saldo_usuario = int(input("Digite seu saldo atual neste momento:\n"))
                usuario.append(saldo_usuario)
        registro.append(usuario)
    return registro

def exibir_registro(registro):
    for i in range(len(registro)):
        print(registro[i])

def upgrade_registro(registro):
    condicao = False
    numero_operacao = int(input("Numero de operacoes efetuados no dia:\n"))
    if(condicao == False):
        for k in range(numero_operacao):
            numero_conta = int(input("Informe o numero da conta:\n"))
            for i in range(len(registro)):
                for d in range(len(registro[0])):
                    if(registro[i][d] == numero_conta):
                        print("Saudacoes %s, o saldo atual da sua conta R$:%s"%(registro[i][d-1],registro[i][d+1]))
                        executar_metodo = raw_input("Digite a sua opcao para (C)- Credito ou (D)-Debito:\n")
                        if(executar_metodo == "C" or executar_metodo == "c"):
                            inserir_quantia = int(input("Inserir a quantia para o credito da conta:\n"))
                            registro[i][d+1] = (registro[i][d+1] - inserir_quantia)
                            condicao = True
                        if(executar_metodo == "D" or executar_metodo == "d"):
                            inserir_quantia = int(input("Inserir a quantia para o debito da conta:\n"))
                            registro[i][d+1] = (registro[i][d+1] - inserir_quantia)
                            condicao = True


numero_usuario = int(input("Boas-vindas,informe quantos clientes existem:\n"))
registro = produzir_registros(numero_usuario)
exibir_registro(registro)
print ("Renovar os dados")
upgrade_registro(registro)
print ("Dados da conta do usuario renovados:")
exibir_registro(registro)
