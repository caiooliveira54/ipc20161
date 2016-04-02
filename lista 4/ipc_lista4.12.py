#Beatriz Pessoa Longato 1615310001
#Equipe 3
#Algoritmo criado no python 2.7.10
#Sintam-se livres para fazer alterações e atualizações

quantidade_alunos= 30

idade= []

altura= []

media= 0

soma=0

num_alunos=0

for i in range (quantidade_alunos):
    
    
    idad= int(input("Digite a idade do aluno: "))
    
    idade.append(idad)
    
    alt= float(input("Digite a altura do aluno: "))
    
    altura.append(alt)
    

for i in altura:
        
    soma += i
    
media= round((soma / quantidade_alunos) , 2)

for i in range (quantidade_alunos):
    
    if (idade[i] > 13 and altura[i] < media):
        num_alunos +=1
        
print(media)
print (num_alunos)



    
    
    
    
    
    
