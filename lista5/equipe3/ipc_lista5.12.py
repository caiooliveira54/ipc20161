#Coding: utf-8
#Introducao a programacao de computadores
#Professor: Jucimar Junior
#samuel silva de frança - 1615310049
#bruno de oliveira freire - 1615310030
#Felipe Henrique Bastos Costa - 1615310032

def fazer_cadastro(funcionario):
    cadastros = []
    for i in range(funcionario):
        dados = []
        for j in range(9):
            if j == 0:
                nome = input("Informe o nome do %dº funcionario: "%(i+1))
                dados.append(nome)
            if j == 1:
                salario = float(input("Salario: "))
                dados.append(salario)
            if j == 2:
                extra_diurna = int(input("Quantas horas extras diurnas?\n"))
                dados.append(extra_diurna)
            if j == 3:
                extra_noturna = int(input("Quantas horas extras noturnas?\n"))
                dados.append(extra_noturna)                
            if j == 4:
                dependente = int(input("Quantos dependentes?\n"))
                dados.append(dependente)
            if j == 5:
                faltas = int(input("Quantas faltas(responder em horas)?\n"))
                dados.append(faltas)
            if j == 6:
                descontos = float(input("Quanto de desconto eventual?\n"))
                dados.append(descontos)
            if j == 7:
                refeicoes = float(input("Quanto gasto em refeicoes feitas na empresa?\n"))
                dados.append(refeicoes)
            if j == 8:
                vales = float(input("Quanto de vales?\n"))
                dados.append(vales)
        cadastros.append(dados)
    return cadastros

def fazer_folha(matriz):
    funcionarios = [["Nome","Salario","Horas extras","salario familia","Salario bruto","Descontos","Salario liquido"]]
    salario_minimo = int(input("Informe o salario familia vigente: "))
    for i in range(len(matriz)):
        dados = []
        horas_extras = (matriz[i][2] * (matriz[i][1]/160))+(matriz[i][3]*1.2*(matriz[i][1]/160))
        salario_familia = matriz[i][4]*0.05*salario_minimo
        salario_bruto = matriz[i][1] + horas_extras + salario_familia
        inamps = 0.08 * matriz[i][1]
        faltas = matriz[i][4]*(matriz[i][1]/160)
        refeicoes = matriz[i][7]
        vales = matriz[i][8]
        descontos_eventuais = matriz[i][6]
        imposto_renda = 0.08 * salario_bruto
        total_descontos = inamps + faltas + refeicoes + vales + descontos_eventuais + imposto_renda
        salario_liquido = salario_bruto - total_descontos        
        dados.append(matriz[i][0])
        dados.append(matriz[i][1])
        dados.append(horas_extras)
        dados.append(salario_familia)
        dados.append(salario_bruto)
        dados.append(total_descontos)
        dados.append(salario_liquido)
        funcionarios.append(dados)
    return funcionarios

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print matriz[i]
        
def mostrar_folha(funcionarios):
    for i in range(len(funcionarios)):
        if i == 0:
            print ["%s"%funcionarios[i][0],"%s"%funcionarios[i][1],"%s"%funcionarios[i][2],"%s"%funcionarios[i][3],"%s"%funcionarios[i][4],"%s"%funcionarios[i][5],"%s"%funcionarios[i][6]]
        else:
            print ["%s"%funcionarios[i][0],"R$ %.2f"%funcionarios[i][1],"R$ %.2f"%funcionarios[i][2],"R$ %.2f"%funcionarios[i][3],"R$ %.2f"%funcionarios[i][4],"R$ %.2f"%funcionarios[i][5],"R$ %.2f"%funcionarios[i][6]]
qtd_funcionarios = int(input("Informe o numero de funcionarios da empresa:\n"))
funcionario = fazer_cadastro(qtd_funcionarios)
folha_pagamento = fazer_folha(funcionario)
mostrar_folha(folha_pagamento)
