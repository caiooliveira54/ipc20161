#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 2
#
#Ana Beatriz Frota  - 1615310027 
#Kylciane Cristiny Lopes Freitas - 1615310052
#Frankilin Yuri Gonçaves dos santos - 1615310033
#


lista1 = []
lista2 = []
v = 10
cont1 = 0
cont2 = 1

while cont1 < v:
    x = float(input("Informe o %dº numero para colocar em sua lista:\n"%cont2))#x recebe o numero a ser colocado na lista;
    lista1.append(x)
    cont1+=1
    cont2+=1
i = len(lista1)-1#novo contador para realizar a inversão dos termos da lista1;

while i >= 0:
    y = lista1[i]#y recebe o ultimo termo da lista1;
    lista2.append(y)#esse termo e colocado no inicio da lista2;
    i= i-1#esse contador esta sendo decrementado para fazer o mesmo processo de pegar os numeros da lista1 e coloca-los
          #na ordem inversa dentro da lista2;
print("A lista invertida é:\n%s"%lista2)
