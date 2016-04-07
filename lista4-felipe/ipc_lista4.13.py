#
#Programa Lista 4, questão 13;
#Felipe Henrique Bastos Costa - 1615310032;
#
mes = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"] # Vetor com todos os meses do ano
temp = [] # Vetor que receberá todos as temperaturas dos meses do ano
soma = 0 # Acumulador que irá somar todas as temperaturas
cont1 = 1 # Condador que funcionará para determinar qual mês está solicitando a temperatura
cont2 = 1 # Contador que mostrará o número de cada linha (Estética)

for i in range (12): # Enquanto estiver ao alcance de 12 índices...
    x = float(input("Informe a temperatura do %dº mês do ano em ºC:\n"%cont1)) # Solicitará elementos ao usuário
    temp.append(x) # Adicionando as temperaturas ao vetor 'temp'
    soma += x # Somatório das temperaturas
    cont1 += 1
    
media_anual = (soma)/12

for i in range(12): # Verificará todos os elementos do vetor
    if(temp[i] > media_anual): # Quais forem maiores que a média
        print("%d- %s = %s"%(cont2,mes[i],temp[i])) # Serão impressos
        cont2 += 1
