# Nickso Patrick Façanha Calheiros - 1615310059

vetcont = []
venda_no_mes = []
quest = ["a", "b","c","d","e","f","g","h","i"]
ac = 0
cond = True

while cond:
    venda = float(input("Digite sua venda bruta no mês(-1 para sair): R$ "))
    bruto = 200.00 +((venda * 9)/100.00)
    venda_no_mes.append(bruto) 
    if venda == -1:
        cond = False
v = len(quest)
ind = len(venda_no_mes)

for i in range(v):
    vetcont.append(ac)
for i in range(ind):
    if venda_no_mes[i] >= 200 and venda_no_mes[i] <= 299:
        vetcont[0]+=1
    if venda_no_mes[i] >= 300 and venda_no_mes[i] <= 399:
        vetcont[1]+=1
    if venda_no_mes[i] >= 400 and venda_no_mes[i] <= 499:
        vetcont[2]+=1
    if venda_no_mes[i] >= 500 and venda_no_mes[i] <= 599:
        vetcont[3]+=1
    if venda_no_mes[i] >= 600 and venda_no_mes[i] <= 699:
        vetcont[4]+=1
    if venda_no_mes[i] >= 700 and venda_no_mes[i] <= 799:
        vetcont[5]+=1
    if venda_no_mes[i] >= 800 and venda_no_mes[i] <= 899: 
        vetcont[6]+=1
    if venda_no_mes[i] >= 1000:
        vetcont[7]+=1
for i in range(v):
    print ("%d Vendedores no intervalo %s" %(vetcont[i],quest[i]))
