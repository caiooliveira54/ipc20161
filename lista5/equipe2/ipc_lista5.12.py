#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Kid Mendes de Oliveira Neto - 1615310011
#Eduardo Maia Freire - 1615310003
#Igor Menezes Sales Vieira - 1615310007
#

def registro_contratado(registro):
    protocolo = []
    for r in range(registro):
        folha = []
        for f in range(9):
            if(f == 0):
                nome_completo = raw_input("Nome completo do funcionario:")
            if(f == 1):
                remuneracao = float(input("Informe seu salario:"))
            if(f == 2):
                horas_extras_diurnas = int(input("Horas extras diurnas trabalhadas:"))
            if(f == 3):
                horas_extras_noturnas = int(input("Horas extras noturnas trabalhadas:"))
            if(f == 4):
                numero_dependentes = int(input("Numero de dependentes do funcionario:"))
            if(f == 5):
                horas_falta = int(input("Quantidade de horas faltadas pelo funcionario:"))
            if(f == 6):
                desconto_evento = float(input("Quantidade de desconto nos eventos:"))
            if(f == 7):
                gasto_refeicao = float(input("Informe os gastos com refeicoes na empresa:"))
            if(f == 8):
                vales_mensal = int(input("Quantos vales retirados no mes? "))
                folha.append(nome_completo)
                folha.append(remuneracao)
                folha.append(horas_extras_diurnas)
                folha.append(horas_extras_noturnas)
                folha.append(numero_dependentes)
                folha.append(horas_falta)
                folha.append(desconto_evento)
                folha.append(gasto_refeicao)
                folha.append(vales_mensal)
        protocolo.append(folha)
    return protocolo
def determinar_salario(registro):
    sal_min = float(input("Informe o salario minimo da empresa:"))
    folha = []
    for i in range(len(registro)):
        contratado = []
        for r in range(1):
            contratado.append(registro[i][0])
            remuneracao = registro[i][1]
            horas_extras = (((registro[i][2])*remuneracao)/160) + (((registro[i][3])*1.2*remuneracao)/160)
            salario_familia = ((registro[i][4])*0.05*sal_min)
            salario_bruto = remuneracao + horas_extras + salario_familia
            inamps = 0.08 * remuneracao
            faltas = ((registro[i][5])*remuneracao)/160
            imposto_renda = 0.08 * salario_bruto
            descontos = (inamps + faltas + (registro[i][7]) + (registro[i][8]) + (registro[i][6]) + imposto_renda)
            salario_liquido = salario_bruto - descontos
            contratado.append(salario_liquido)
            contratado.append(salario_bruto)
            contratado.append(descontos)
            contratado.append(horas_extras)
            folha.append(contratado)
    return folha

def exibir_ficha(ficha):
    for i in range(len(ficha)):
        print("Boas-vindas %s,seu salario bruto sera: R$%.2f"%(ficha[i][0],ficha[i][2]))
        print("Horas extras:R$%.2f"%ficha[i][4])
        print("Desconto total:R$%.2f"%ficha[i][3])
        print("Salario liquido:R$%.2f"%ficha[i][1])

numero_contratado = int(input("Informe o numero de funcionarios da empresa:"))
registro = registro_contratado(numero_contratado)
ficha = determinar_salario(registro)
exibir_ficha(ficha)
