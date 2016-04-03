#
#Programa Lista 4, questão 15;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista = []
listainv = []
cond = True
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
soma = 0

while(cond):
    nota = float(input("Informe uma nota(para encerrar o programa, informe -1):\n"))
    if(nota == -1):
        soma = soma
        cont1 = cont1
        cond = False
    else:
        lista.append(nota)
        soma += nota
        cont1 += 1
media_notas = (soma)/cont1
v = cont1 - 1

while(cont2 <= v):
    x = lista[v]
    listainv.append(x)
    v -= 1
    
for i in range(cont1):
    if(lista[i] > media_notas):
        cont3 += 1
    if(lista[i] < 7):
        cont4 += 1
print("A quantidade de valores lidos foi de %d"%cont1)
print("Os valores informados foram:\n%s"%lista)
print("A lista inversa, com os elementos um abaixo do outro e:")
for i in range(cont1):
    print(listainv[i])
print("A soma dos valores dentro da lista e: %.2f"%soma)
print("A media geral das notas e: %.2f"%media_notas)
print("A quantidade de notas acima da media geral e(sao): %d"%cont3)
print("A quantidade de notas abaixo de sete e(sao): %d"%cont4)
print("Obrigado por usar nossos serviços!")