#
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#
maior_acerto = 0
menor_acerto = 10
total_alunos = 0
total_notas = 0
media_alunos = 0
gabarito = ["A","B","C","D","E","E","D","C","B","A"]
print("Respostas apenas em MAIUSCULO.")
continuar = True
while continuar:
    total_alunos = total_alunos + 1
    nota_aluno = 0
    questao = 0
    while questao < 10:
        resposta = input("Digite a resposta da questao " + str(questao + 1) + ": ")
        if(resposta == gabarito[questao]):
            nota_aluno = nota_aluno + 1
        questao = questao + 1
    print("Nota aluno: ", nota_aluno)

    if(nota_aluno > maior_acerto):
        maior_acerto = nota_aluno
    if(nota_aluno < menor_acerto):
        menor_acerto = nota_aluno

    total_notas = total_notas + nota_aluno
    

    continuar = input("Outro aluno vai utilizar o sistema(S/N): ")
    if (continuar == "S" or continuar == "s"):
        continuar = True
    elif (continuar == "N" or continuar == "n"):
        continuar = False
    else:
        while (continuar != "S" and continuar != "s" and continuar != "N" and continuar != "n"):
            continuar = input("Opcao invalida, digite outra opcao(S/N): ")

print("Total de alunos: ", total_alunos)
media_turma = total_notas / total_alunos
print("Media da turma: ", media_turma)
