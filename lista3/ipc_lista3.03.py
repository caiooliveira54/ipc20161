#
#Ana Jessye 1615310046
#Franklin Yuri 1615310033
#Kylciane Freitas 1615310032
#Madson Lemos 1615310037
#IPC_Lista3.4
#

nome = input("Informe seu nome: ")

while (len(nome) <=3):
    print ("Seu nome deve ter mais de 3 caracteres!")
    nome = input("Informe seu nome: ")

idade = int(input("Informe sua idade: "))

while (idade <0 or idade >150):
    print ("A idade deve ser entre 0 e 150!")
    idade = int(input("Informe sua idade: "))
     
salario = float(input("Informe seu salario: "))

while (salario <=0):
    print ("Seu salario deve ser maior que 0")
    salario = float(input("Informe seu salario: "))

sexo = input("Informe seu sexo: (m/f)")

while (not(sexo == 'm' or sexo == 'f')):
    print("Informação Errada!")
    sexo = input("Informe seu sexo: (m/f)")
    
estado_civil = input("Informe seu estado civil: (s,c,d,v)")

while (not(estado_civil =="s" or estado_civil =="c" or estado_civil =="d" or estado_civil =="v")):
    print("Informação Errada!")
    estado_civil = input("Informe seu estado civil: (s,c,d,v)")
    
print ("Informações aceitas!")
print ("Nome: ",nome, "\n Idade: ",idade, "\n Salario: ", salario, "\n Sexo: ",sexo, "\n Estado_Civil: ",estado_civil)

