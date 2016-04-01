#Beatriz Pessoa Longato 1615310001

media= [] # Vetor que irá receber e armazenar todas as médias que serão calculadas

quantidade_alunos= 10 # Aqui determina quantos alunos tem na sala

cont= 1 # Contador que será incrementado a cada volta até a condição ser desobedecida

quantidade_notas= 4 # Quantidade de notas que cada aluno deve ter (Obs.: Onde tem a funcionalidade dessa variável? Pelo que vi, era para ser usada na média, não?)

nota1=0 # A variável que armazenará a nota 1 do usuário 
nota2=0 # A variável que armazenará a nota 2 do usuário
nota3=0 # A variável que armazenará a nota 3 do usuário
nota4=0 # A variável que armazenará a nota 4 do usuário
num_aluno=0 # Acumulador que receberá valores se a condição (bem abaixo), for verdadeira

m=0  # Variável que receberá a média de cada aluno após somar todas as notas e dividir por 4

while cont <= quantidade_alunos: # Enquanto esta condição for verdadeira...
    
    nota1=float(raw_input("Digite a nota 1: ")) # ... Solicitará ao usuário a nota 1
    
    nota2=float(raw_input("Digite a nota 2: ")) # ... E solicitará ao usuário a nota 2
    
    nota3=float(raw_input("Digite a nota 3: ")) # ... E solicitará ao usuário a nota 3
    
    nota4=float(raw_input("Digite a nota 4: ")) # # ... E solicitará ao usuário a nota 4
    
    cont +=1 # Contador que será incrementado até a condinção do while ser falsa
    
    m=(nota1 + nota2 + nota3 + nota4) / 4 # Variável que calculará a média de cada aluno
    
    media.append(m) # Após calcular a média, será armazenada no vetor 'media'
    
    
    if m >= 7: # Se a média for maior do que 7.0...
        
        num_aluno +=1 # ... Acumulará mais um aluno até verificar todos os alunos


print (num_aluno) , "alunos tiveram média maior ou igual a 7." # Impressão do número de alunos com êxito no exame
