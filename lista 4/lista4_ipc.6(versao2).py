#Beatriz Pessoa Longato 1615310001

media= []

quantidade_alunos= 10

cont= 1

quantidade_notas= 4

nota1=0
nota2=0
nota3=0
nota4=0
num_aluno=0

m=0

while cont <= quantidade_alunos:
    
    nota1=float(raw_input("Digite a nota 1: "))
    
    nota2=float(raw_input("Digite a nota 2: "))
    
    nota3=float(raw_input("Digite a nota 3: "))
    
    nota4=float(raw_input("Digite a nota 4: "))
    
    cont +=1
    
    m=(nota1 + nota2 + nota3 + nota4) / 4
    
    media.append(m)
    
    
    if m >= 7:
        
        num_aluno +=1


print (num_aluno) , "alunos tiveram média maior ou igual a 7."