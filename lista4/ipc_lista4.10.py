#
#Programa Lista 4, questão 10;
#Felipe Henrique Bastos Costa - 1615310032;
#

lista1 = []#Lista vazia;
lista2 = []#Lista vazia;
lista3 = []#Lista vazia que armazenara os termos da lista1 e lista2;
v1 = 10#representaria o len das duas primeiras listas
cont1 = 0#contador que representaria o indice da lista
cont2 = 1#contador para saber qual a posição do elemento na lista, se e o primeiro ou segundo etc;

while(cont1 < v1):
    x1 = raw_input("Informe o %dº elemento a ser colocado na primeira lista:\n"%cont2)#pedindo para o usuario informar o 
    x2 = raw_input("Informe o %dº elemento a ser colocado na segunda lista:\n"%cont2) #elemento que deseja colocar na lista;
    lista1.append(x1)#ele adicionara o x1(elemento dado pelo usuario) na lista1
    lista2.append(x2)#ele adicionara o x2(elemento dado pelo usuario) na lista2
    lista3.append(x1) #como ele quer a lista3 de com os elementos da lista 1 e 2 de forma alternada
    lista3.append(x2) #coloca-se na lista3 tanto x1 quanto x2, mas em append's diferentes;
    cont1+=1#incrementando o contador do indice;
    cont2+=1#incrementando a posição do elemento na lista;

print("A uniao das listas de forma alternada e:\n%s"%lista3)