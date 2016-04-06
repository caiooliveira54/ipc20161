"""
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura 
inferior à média de altura desses alunos.
"""
idade = []
altura = []
v = 30
media = 0
alunos = 0
soma = 0

for i in range (v):
    x = (int(input("idade do aluno: ")))
    y = (float(input("altura do aluno: ")))
    idade.append(x)
    altura.append(y)

for i in (altura):
    soma += i
    
media = round((soma / v),2)

for i in range(v):
    if (idade[i] > 13 and altura[i] < media):
        alunos += 1
        
print ("A media da altura:",media)
print ("Alunos acima de 13:", alunos)