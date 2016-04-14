#professor jucimar junior
#Bruno de Oliveira freire - 1615310030
#Felipe Henrique Bastos Costa -1615310032
#Caio de OLiveira Martins-1615310031
#Samuel Silva de França- 1615310049
#Eduardo Maia Freire-1615310003
#lista de Repetição

sal_inicial = float(1000)

cont1 = 1995
cont2 = 0.015

while (cont1 < 2016):
    sal_final = sal_inicial + (sal_inicial*cont2)
    cont2 = cont2 * 2
    cont1 = cont1 +1
print("Salario atual é: %.2f" %sal_final)
