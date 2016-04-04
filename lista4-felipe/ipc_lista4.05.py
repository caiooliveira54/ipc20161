#
#Programa Lista 4, questão 5;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista = []
par = []
impar = []
v = 20
cont1 = 0
cont2 = 1

while(cont1 < v):
    x = int(input("Informe o %dº numero de sua lista de 20 números:\n"%cont2))
    lista.append(x)
    if(lista[cont1]%2==0):
        par.append(x)
    else:
        impar.append(x)
    cont1+=1
    cont2+=1
print("A lista completa e:\n%s\nOs numeros pares sao:\n%s\nOs impares sao:\n%s"%(lista,par,impar))
