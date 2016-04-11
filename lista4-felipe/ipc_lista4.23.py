#
#Programa Lista 4, questão 23;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista_nome = []
lista_tamanho = []
lista_porcento = []
por_cento = "%"
soma = 0
cont1 = 0
cont2 = 1

for i in range(6):
    nome = raw_input("%dº Nome:\n"%cont1)
    lista_nome.append(nome)
    espaco_memoria = float(input("Informe o espaco ocupado em bytes:\n"))
    megabyte = espaco_memoria/1048576
    lista_tamanho.append(megabyte)
    soma += megabyte
    cont1 += 1
    
for i in lista_tamanho:
    porcento = i * 100/soma
    lista_porcento.append(porcento)
media = soma/6

print("-"*50+"\nNr."+" "*3+"Usuario"+" "*5+"Espaco utilizado"+" "*3+"% do uso")
for i in range(cont1):
    print("%d.   %s     %.2fMB           %.2f%s"%(cont2,lista_nome[i],lista_tamanho[i],lista_porcento[i],por_cento))
    cont2 += 1
print("Espaco total ocupado: %.2fMB\nEspaco medio ocupado: %.2fMB"%(soma,media))