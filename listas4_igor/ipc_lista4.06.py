#
#Igor Menezes Sales Vieira - Matricula: 1615310007
#
media = [] # Vetor que receberá todas as médias
acm = 0
cont = 1
acm_media = 0
cont_media = 0
mediax = 0
i = 1
while i < 5: # Enquanto estiver nesta condição...
    print("%d° aluno"%i) # Imprimirá o número do aluno...
    cont = 1
    acm = 0
    acm_media = 0
    mediax = 0
    while cont < 5:
        nota = float(input("Digite a nota:")) # Solicitará a ele suas 4 notas
        acm = acm + nota # Acumulará as notas
        cont = cont + 1 # Incremento do contador
    acm_media = acm_media + acm
    mediax = (acm_media)/4 # Calculo da media
    media.append(mediax) # Acrescentando a media calculada ao vetor media
    if mediax >= 7: # Se a media for maior ou igual a sete
        cont_media = cont_media + 1 # o contador sera acrescido de 1
    print("Media:",media[(i-1)]) # Imprimira a media
    i = i + 1
print("Alunos aprovados:%d"%cont_media) # Imprimira o numero de alunos com media maior ou igual a sete
