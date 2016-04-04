#
#Programa Lista 4, questão 3;
#Felipe Henrique Bastos Costa - 1615310032;
#
notas = [] # Vetor que receberá as quatro notas do aluno
v = 4 # 'v' Limitará o contador 
cont1 = 0 # Contador que indicará o índice do elemento na lista e servirá para ser incrementado até a condição ser False
cont2 = 1 # COntador para acrescentar 'estética' à variável x que irá solicitar uma nota 1, 2, 3 ou 4
soma = 0 # Acumulador para receber todas as notas e armazená-las

while(cont1 < v):
    x = float(input("Informe a nota do %dº bimestre:\n"%cont2))
    notas.append(x) # Adicionará todas as notas ao vetor 'notas'
    soma+=notas[cont1] # Acumulando os valores da lista
    cont1+=1 # Incremento do contador 1
    cont2+=1 # Incremento do contador 2
print("A media das notas dos quatro bimestres e de %.2f"%(soma/v)) # Impressão da media final
