#
#Programa Lista 4, questão 12;
#Felipe Henrique Bastos Costa - 1615310032;
#
idade = [] # Vetor que receberá todas as idades dos alunos
altura = [] # Vetor que receberá todas as alturas dos alunos
cont1 = 1
cont2 = 0
soma = 0 # Somatório das alturas dos alunos

for i in range(30): # Enquanto estiver ao alcance...
    x = int(input("Informe a idade da %dº pessoa:\n"%cont1)) # Solicitará as idades  
    y = float(input("Informe a altura da %dº pessoa:\n"%cont1)) # e alturas
    idade.append(x)
    altura.append(y)
    soma += y
    cont1 += 1
media_altura = (soma)/30 # Calcula a media

for i in range(30): # Percorrerá todas as alturas e comprarará coma as médias
    if(idade[i] > 13 and altura[i] < media_altura):
        cont2 += 1
    else:
        cont2 = cont2
print("%d alunos sao mais baixos que a media dos demais e sao maiores que 13 anos"%cont2) # Imprimirá todos os alunos com mais de 13 anos e são abaixo da média
