#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 3
#
#Antonio Rodrigues de Souza Neto - 1615310028
#Caio de Oliveira Martins - 1615310031
#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#

nome = ("Informe seu nome: ")

while (len(nome) <=3):
    print ("Seu nome deve ter mais de 3 caracteres!")
    nome = input("Informe seu nome: ")

idade = int(input("Informe sua idade: "))

while (idade <0 or idade >150):
    print ("A idade deve ser entre 0 e 150!")
    nome = input("Informe seu nome: ")
     
salario = float(input("Informe seu salario: "))

while (salario <=0):
    print ("Seu salario deve ser maior que 0")
    salario = float(input("Informe seu salario: "))

sexo = input("Informe seu sexo:(m/f)")

while (sexo != "m" or sexo != "f"):
    print("Informação Errada!")
    sexo = input("Informe seu sexo:(m/f)")
    
estado_civil = input("Informe seu estado civil: (s,c,d,v)")

while (estado_civil !="s" or estado_civil !="c" or estado_civil !="d" or estado_civil !="v"):
    print("Informação Errada!")
    estado_civil = input("Informe seu estado civil: (s,c,d,v)")
    
print ("Informações aceitas!")
print ("Nome: ",nome, "Idade: ",idade, "Salario: ", salario, "Sexo: ",sexo, "Estado_Civil: ",estado_civil)
