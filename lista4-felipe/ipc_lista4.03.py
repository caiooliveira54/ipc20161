#
#Programa Lista 4, questão 3;
#Felipe Henrique Bastos Costa - 1615310032;
#
notas = []
v = 4
cont1 = 0
cont2 = 1
soma = 0

while(cont1 < v):
    x = float(input("Informe a nota do %dº bimestre:\n"%cont2))
    notas.append(x)
    soma+=notas[cont1]
    cont1+=1
    cont2+=1
print("A media das notas dos quatro bimestres e de %.2f"%(soma/v))
