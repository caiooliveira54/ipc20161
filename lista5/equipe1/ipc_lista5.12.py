def cadastrar_funcionarios(funcionarios, colunas):
    cadastros = []
    for i in range(funcionarios):
        ficha = []
        for j in range(colunas): # Colunas = 9
            if j == 0:
                nome = str(input("\nQual o nome do funcionario? "))
                ficha.append(nome)
            if j == 1:
                salario = float(input("Qual o salario do funcionario? "))
                ficha.append(salario)
            if j == 2:
                hed = float(input("Quantas horas extras diurnas trabalhadas? "))
                ficha.append(hed)
            if j == 3:
                hen = float(input("Quantas horas extras noturnas trabalhadas? "))
                ficha.append(hen)
            if j == 4:
                nd = int(input("Qual o numero de dependentes deste funcionario? "))
                ficha.append(nd)
            if j == 5:
                faltas = int(input("Qual o total de horas faltadas? "))
                ficha.append(faltas)                
            if j == 6:
                descontos = float(input("Quais os descontos eventuais? "))
                ficha.append(descontos)
            if j == 7:
                refeiçao = float(input("Qual o valor total gasto em refeiçoes? "))
                ficha.append(refeiçao)
            if j == 8:
                vales = float(input("Quanto em vales foi retirado por este funcionario? "))
                ficha.append(vales)
        cadastros.append(ficha)
    return cadastros

def calcular_liquido(cadastros):
    salario_minimo = int(input("\nQual o salario minimo vigente? "))
    folha = []
    for i in range(len(cadastros)):
        funcionario = []
        for j in range(1):
            funcionario.append(cadastros[i][0])
            salario = cadastros[i][1]
            hed = ((cadastros[i][2] * salario )/ 160)
            hen = ((cadastros[i][3] * 1.2 * salario ) / 160)
            extra = hed + hen
            salario_familia = (cadastros[i][4] * 0.05 * salario_minimo)
            salario_bruto = salario + extra + salario_familia #
            inamps = 0.08 * salario
            falta = ((cadastros[i][5] * salario) / 160)
            refeiçoes = cadastros[i][7]
            vales = cadastros[i][8]
            descontos_eventuais = cadastros[i][6]
            imposto_renda = salario_bruto * 0.08
            desconto_total = inamps + falta + refeiçoes + vales + descontos_eventuais + imposto_renda 
            salario_liquido = salario_bruto - desconto_total
            funcionario.append(salario_liquido)
            folha.append(funcionario)
    return folha

def imprimir_folha(folha):      
    for i in range(len(folha)): 
        print ("Funcionario %s possui salario liquido equivalente a R$%.2f"%(folha[i][0], folha[i][1]))
        print ("----------------------------------------------------------------------------")
        
print ("\nCadastros dos funcionarios da empresa")
funcionarios = int(input("\nQuantos funcionarios ativos possuem a empresa? "))
colunas = 9
cadastros = cadastrar_funcionarios(funcionarios, colunas)

folha = calcular_liquido(cadastros)
print ("\nFolha de pagamento:\n")
imprimir_folha(folha)
            
            

            
        
