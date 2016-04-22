#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 4
#
#Bruno de Oliveira Freire - 1615310030
#Igor Menezes Sales Vieira - 1615310007
#Matheus Mota de Souza - 1615310016
#Nadine da Cunha Brito - 1615310040
#Nickso Patrick Façanha Calheiros - 1615310059
#Thiago Santos Borges - 1615310023
#

q_turmas=int(input("informe a quantidade de turmas:\n"))
cond=0
q_total=0
numeroturma=0

while(cond<q_turmas):
    numeroturma+=1
    q_alunos=int(input("informe a quantidade de alunos da turma %d:"%numeroturma))
    q_total=q_total + q_alunos
    media_turma=q_total/q_turmas
    if (q_alunos>40):
        print("quantida de alunos invalida")
        cond=cond
        
        
    elif (q_alunos>0 and q_alunos<40):
        cond+=1
        q_alunos=q_alunos + q_alunos
        
print("a media de aluno por turma e:%d"%media_turma)
