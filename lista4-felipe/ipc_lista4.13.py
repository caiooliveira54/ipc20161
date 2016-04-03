#
#Programa Lista 4, questão 13;
#Felipe Henrique Bastos Costa - 1615310032;
#
mes = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
temp = []
soma = 0
cont1 = 1
cont2 = 1

for i in range (12):
    x = float(input("Informe a temperatura do %dº mês do ano:\n"%cont1))
    temp.append(x)
    soma += x
    cont1 += 1
    
media_anual = (soma)/12

for i in range(12):
    if(temp[i] > media_anual):
        print("%d- %s = %s"%(cont2,mes[i],temp[i]))
        cont2 += 1