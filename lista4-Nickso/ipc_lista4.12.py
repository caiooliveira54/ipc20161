#Nickso Patrick Façanha Calheiros - 1615310059

vidade = []
valtura = []
cont = 0
media = 0
div = 1
arm = 0
while cont < 30:
    idade = float(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    media = (altura + media)/div
    div += 1
    cont += 1
    if idade > 13 and altura < media:
        arm += 1
print ("Quantidade de alunos abaixo da media",arm)
print ("Media de altura dos alunos %5.2f" % media)
