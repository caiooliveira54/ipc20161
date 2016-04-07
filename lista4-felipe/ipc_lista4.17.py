#
#Programa Lista 4, questão 17;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista_saltos = []
lista_nomes = []
lista_media = []
cond = True
cont1 = 1
cont2 = 0
soma = 0

print("O programa será feito para uma competição de saltos a distancia")
print("Quando quiser parar o programa, basta não informar nenhum nome e pressionar enter")
while cond:
    nome = raw_input("Atleta:\n")
    if nome == "":
        cond = False
    else:
        for i in range(5):
            salto = float(input("Informe a distancia do %dº salto:\n"%cont1))
            lista_saltos.append(salto)
            soma += salto
            cont1 += 1
            if cont1 == 6:
                cont1 = 1
        cont2 += 1
        media = (soma)/5
        soma = 0
        lista_media.append(media)
    lista_nomes.append(nome)
v = 5
cont3 = 0

print("Resultado final:")
for i in range(cont2):
    print("Atleta: %s"%lista_nomes[i])
    print("Saltos: %.2f - %.2f - %.2f - %.2f - %.2f"%(lista_saltos[cont3],lista_saltos[cont3+1],lista_saltos[cont3+2],lista_saltos[cont3+3],lista_saltos[cont3+4]))
    cont3 += 5
    v += 5
    print("Media: %.2f"%lista_media[i]) 
