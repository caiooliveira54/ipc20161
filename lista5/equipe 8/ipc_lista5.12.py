#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Matheus Palheta Barbosa - 1615310019
#Any Mendes Carvalho - 1615310044
#Victor Rafael da Silva e Silva - 1615310025
#

from matriz import*

salario_minimo = 800
               #nome, salario, horas extras dirunas, horas extras noturnas, dependentes, faltas, descontos, refeicao, vales
funcionarios = [["Matheus", 1500, 0, 0, 0, 0, 0, 0, 0],
                ["Lucas", 1500, 5, 5, 2, 5, 12, 1, 1],
                ["Pedro", 1500, 10, 10, 3, 0, 0, 0, 0]]

for func in funcionarios:
    print("Nome: ", func[0])
    print("Salario Base: ", func[1])
    
    horas_extras = (func[2] * func[1]/160) + (func[3] * 1.2 * func[1]/160)
    
    print("Horas extras: ", horas_extras)
    
    salario_familia = func[4] * 0.05 * salario_minimo
    
    print("Salario familia: ", salario_familia)
    
    salario_bruto = func[1] + horas_extras + salario_familia
    
    print("Salario bruto: ", salario_bruto)
    
    inamps = 0.08 * func[1]
    faltas = func[5] * func[1]/160
    
    descontos = inamps + faltas + func[6] + func[7] + func[8]
    
    salario_liquido = salario_bruto - descontos
    
    print("Salario liquido: ", salario_liquido)
    print();