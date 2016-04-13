# Mateus Mota de Souza = 1615310016
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
temp = []
acm = 0

for i in range(12):
    celsius = float(input("Insira uma temperatura para o mes %s: "%(meses[i])))
    temp.append(celsius)
    acm += celsius
    media = acm/12

print ("\nMedia anual: %.2f" %media)
for i in range(12):
    if temp[i] > media:
        print ("Ocorreu no mes:", meses[i],"| Temperatura:", temp[i])
        

