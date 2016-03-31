# 
# Programa exemplo
# Jucimar Jr 5675767
#

MEDIA_UEA = 6
MEDIA_UEA_PASSOU_DIRETO = 8
QTDE_ALUNOS = 40

contador = 1
somatorio_notas = 0

while contador <= QTDE_ALUNOS:
    nome  = raw_input("Digite seu nome: ")
    nota1 = int(input("Digite a nota 1: "))
    nota2 = int(input("Digite a nota 2: "))
    
    media = (nota1 + nota2)/2
    
    if media >= MEDIA_UEA_PASSOU_DIRETO:
        print("Aprovado direto! Parabens")
    else:
        nota3 = int(input("Digite a nota 3: "))
        media = (nota1+nota2+nota3)/3
    
        if media >= MEDIA_UEA:
            print("Aprovado")
        else:
            print("Reprovado")
    
    print(media)
    somatorio_notas = somatorio_notas + media
    contador = contador + 1
    
media_turma = somatorio_notas/QTDE_ALUNOS

print(media_turma)
