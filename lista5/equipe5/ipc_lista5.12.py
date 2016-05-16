#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 5
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#

def cadastrar_funcionarios(funcionarios):
    cadastro = []
    for j in range(funcionarios):
        linha = []
        for i in range(9):
            if i == 0:
                nome = input("\nQual seu nome: ")
                linha.append(nome[j][0])
            if i == 1:
                sal = float(input("Qual o seu salario mensal: R$"))
                linha.append(sal)
            if i == 2:
                hed = float(input("Horas extras diurnas: "))
                linha.append(hed)
            if i == 3:
                hen = float(input("Horas extras noturnas: "))
                linha.append(hen)
            if i == 4:
                nd = int(input("Numero de dependentes: "))
                linha.append(nd)
            if i == 5:
                faltas = int(input("Horas faltadas: "))
                linha.append(faltas)                
            if i == 6:
                descontos = float(input("Descontos eventuais: "))
                linha.append(descontos)
            if i == 7:
                refeicao = float(input("Valor total gasto em refeiçoes: "))
                linha.append(refeicao)
            if i == 8:
                vales = float(input("Quantidade de vales retirados: "))
                linha.append(vales)
        cadastro.append(linha)
    return cadastro

def calcular_liquido(funcionarios):
    salario_minimo = int(input("\nQual o salario minimo: "))
    folha = []
    for i in range(len(funcionarios)):
        empregados = []
        for j in range(1):
            nome = (funcionarios[i][0])
            empregados.append(nome)
            salario = funcionarios[i][1]
            hed = (funcionarios[i][2] * salario)/ 160
            hen = (funcionarios[i][3] * 1.2 * salario) / 160
            horas_extra = hed + hen
            salario_familia = funcionarios[i][4] * 0.05 * salario_minimo
            salario_bruto = salario + horas_extra + salario_familia 
            inamps = 0.08 * salario
            falta = (funcionarios[i][5] * salario) / 160
            refeiçoes = funcionarios[i][7]
            vales = funcionarios[i][8]
            descontos_eventuais = funcionarios[i][6]
            imposto_renda = salario_bruto * 0.08
            desconto_total = inamps + falta + refeiçoes + vales + descontos_eventuais + imposto_renda 
            salario_liquido = salario_bruto - desconto_total
            empregados.append(salario_liquido)
            folha.append(empregados)
    return folha

def mostrar_folha(folha):
    print ("\nFolha de pagamento mensal")
    for i in range(len(folha)): 
        print ("\nFuncionario %s possui salario liquido equivalente a R$%.2f"%(folha[i][0], folha[i][1]))

empregardos = int(input("Programa de cadastro de funcionarios\nNumero de funcionarios empregados atualmente: "))
cadastramento = cadastrar_funcionarios(empregardos)
folha_de_pagamento = calcular_liquido(cadastramento)
mostrar_folha(folha_de_pagamento)
