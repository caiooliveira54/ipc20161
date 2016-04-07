# Nickso Patrick Façanha Calheiros - 1615310059

lista = []
acima_m = []
abaixo_m = []
ac = 0
soma = 0

while True:
    l = float(input("Digite uma nota (1 sai): "))
    if l == 1:
        break
    lista.append(l)
    ac += 1
    soma += l
c = len(lista)
c = c - 1
while c >= 0:
    print (lista[c])
    c = c - 1
    
print ("Quantidade de valores lidos",ac)
print ("Valores na ordem em que foram informados", lista)
print ("Soma dos Valores:",soma)
print ("Média dos valores: %5.2f" %(soma/ac))
cont = 0
while cont < len(lista):
    if lista[cont] > (soma/ac):
        acima_m.append(lista[cont])
    if lista[cont] < 7:
        abaixo_m.append(lista[cont])
    cont += 1

print ("Valores acima da média: ", acima_m)
print ("Valores abaixo de sete: ", abaixo_m)
print ("Espero tirar 10 na proda de I.P.C.")



