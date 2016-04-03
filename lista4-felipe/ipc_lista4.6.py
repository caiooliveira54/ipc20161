#
#Programa Lista 4, questão 6;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista = []
cont1 = 0 #contador para o numero de loops para os alunos;
cont2 = 1 #contador para saber qual o aluno que esta sendo analisado, se e a primeira ou a segunda e assim por diante;
acm = 0 #acumulador para o numero de medias igual ou acima de sete;
soma = 0#acumulador para as notas de cada aluno;
v1 = 10#representa o len da lista a ser formada;

while(cont1 < v1):
    print("~~%dº aluno~~"%cont2)#apenas para enfeite, indica qual aluno está sendo trabalhado;
    nota1 = float(input("Informe a 1º nota:\n"))
    nota2 = float(input("Informe a 2º nota:\n"))
    nota3 = float(input("Informe a 3º nota:\n"))
    nota4 = float(input("Informe a 4º nota:\n"))
    soma = nota1 + nota2 + nota3 + nota4#realiza a soma das notas para entao
    media = (soma)/4                    #ser feito o calculo da media;
    lista.append(media)#vai pegar as medias e armazenar na lista "lista";
    cont1+=1#ira incrementar o contador, prosseguindo para o proximo aluno;
    cont2+=1#ira incrementar o contador para saber qual aluno estamos lidando;
    if(media >= 7):
        acm+=1#começara a acumular o numero de notas que conseguiram superar a media
print("%d alunos conseguiram uma nota igual ou superior a 7"%acm)