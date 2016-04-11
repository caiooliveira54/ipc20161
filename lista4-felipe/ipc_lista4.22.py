#
#Programa Lista 4, questão 22;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista_qtd = [0,0,0,0]
lista_opcoes = [1,2,3,4]
lista_percentual = []
cont1 = 1
cont2 = 0
cont3 = 1
por_cento ="%"
cond = True
print("Informe a situação que se encontra os mouses digitando o numero de uma das opções a baixo:")
print("1- necessita da esfera\n2- necessita de limpeza\n3- necessita troca do cabo ou conector\n4- quebrado ou inutilizado\n0- parar o programa")

while cond:
    print("~~~%dº mouse~~~"%cont1)
    opcao = int(input("Informe a opcao:\n"))
    if opcao == 0:
        cond = False
    else:
        for i in range(4):
            if lista_opcoes[i] == opcao:
                lista_qtd[i] += 1
                cont2 += 1
    cont1 += 1
for i in range(4):
    percentual = float(lista_qtd[i])*100/cont2
    lista_percentual.append(percentual)
print("Quantidade de mouses: %d"%cont2)
print("Situacao"+" "*40+"Quantidade"+" "*10+"Percentual")
print("1- necessita da esfera"+" "*30+"%d"%lista_qtd[0]+" "*17+"%.2f%s"%(lista_percentual[0],por_cento))
print("2- necessita de limpeza"+" "*29+"%d"%lista_qtd[1]+" "*17+"%.2f%s"%(lista_percentual[1],por_cento))
print("3- necessita troca do cabo ou conector"+" "*14+"%d"%lista_qtd[2]+" "*17+"%.2f%s"%(lista_percentual[2],por_cento))
print("4- quebrado ou inutilizado"+" "*29+"%d"%lista_qtd[3]+" "*17+"%.2f%s"%(lista_percentual[3],por_cento))