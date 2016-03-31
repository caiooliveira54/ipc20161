#professor jucimar junior
#Bruno de Oliveira freire - 1615310030
#Felipe Henrique Bastos Costa -1615310032
#Caio de OLiveira Martins-1615310031
#Samuel Silva de França- 1615310049
#Eduardo Maia Freire-1615310003
#lista de Repetição

num_cds = float(input("Informe a quantidade de cds comprados:\n"))
cond = 1
x1 = 0
x = 0
total = 0

while(cond <= num_cds ):
    x1 += 1
    valor = float(input("Informe o valor do %d CD, em reais:\n"%x1))
    total += valor
    media = total / num_cds
    cond += 1
    
print("O colecionador investiu %.2f reais em sua colecao"%total)
print("A media de gasto, por cd, do colecionador foi de %.2f reais"%media)
