idade = []
altura = []
acm = 0
for i in range(5):
    idadex = int(input("Digite a idade: "))
    alturax = float(input("Digite a altura: "))
    idade.append(idadex)
    altura.append(alturax)
    acm = alturax + acm

media = acm/5

cont = 0
for i in range(5):
    if idade[i]>13:
        if altura<media:
            cont += 1

print("Numero de alunos com altura inferior a media: %d"%cont)
