#
#Programa Lista 4, questão 12;
#Felipe Henrique Bastos Costa - 1615310032;
#
idade = []
altura = []
cont1 = 1
cont2 = 0
soma = 0

for i in range(30):
    x = int(input("Informe a idade da %dº pessoa:\n"%cont1))
    y = float(input("Informe a altura da %dº pessoa:\n"%cont1))
    idade.append(x)
    altura.append(y)
    soma += y
    cont1 += 1
media_altura = (soma)/30

for i in range(30):
    if(idade[i] > 13 and altura[i] < media_altura):
        cont2 += 1
    else:
        cont2 = cont2
print("%d alunos sao mais baixos que a media dos demais e sao maiores que 13 anos"%cont2)