# Nickso Patrick Façanha Calheiros - 1615310059

media_aprovados = []
cont = 0
num_alunos = 0
while cont < 10:
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    nota3 = float(input("Digite sua terceira nota: "))
    nota4 = float(input("Digite sua quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4)/4
    if media >= 7:
        media_aprovados.append(media)
        num_alunos = num_alunos + 1
    cont = cont + 1
print ("%d Alunos foram Aprovados" %num_alunos)
print ("com Medias",media_aprovados)
    

