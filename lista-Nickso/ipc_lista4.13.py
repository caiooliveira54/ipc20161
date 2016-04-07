# Nickso Patrick Façanha Calheiros - 1615310059

temp = []
mes = ["Janeiros", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outeubro", "Novembro", "Dezembro"]
armaz = []
armazmes = []

cont = 0
acum = 0
ind = len(mes)

while cont < ind:
    temperatura = float(input("Digite a temperatura de %s" %mes[cont]))
    temp.append(temperatura)
    acum += temperatura
    cont += 1
    media = acum / len(temp)

for i in range(12):
    if temp[i]>media:
        print("Temperatura acima da media %5.2f-%s" %(temp[i],mes[i]))
