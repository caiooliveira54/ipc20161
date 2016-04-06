#Bruno de Oliveira Freire - 1615310030
media=[]
qtd_alunos=0
num_aluno=0
m=0
aluno=1

for qtd_alunos in range(10):
    print("-------------nota do aluno %d-----------------"%aluno)
    n1=float(input("insira o numero 1:"))
    n2=float(input("insira o numero 2:"))
    n3=float(input("insira o numero 3:"))
    n4=float(input("insira o numero 4:"))
    aluno+=1
    m = (n1+n2+n3+n4)/4
    media.append(m)
    
    if m>=7:
        num_aluno+=1
print("esse e a quantidade de alunos com nota na media:%d"%num_aluno)
