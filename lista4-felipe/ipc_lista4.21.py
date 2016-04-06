#
#Programa Lista 4, questão 18;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista_carro = []
lista_consumo = []
lista_litros_gastos = []
lista_preco = []
v = 5
cont1 = 1
cont2 = 1

for i in range(v):
    print("Veiculo %d"%cont1)
    carro = raw_input("Informe a marca do carro:\n")
    consumo = float(input("Km por litro:\n"))
    lista_carro.append(carro)
    lista_consumo.append(consumo)
    litros = 1000/(consumo)
    preco = (litros)*(2.25)
    lista_litros_gastos.append(litros)
    lista_preco.append(preco)
    cont1 += 1

economico = lista_litros_gastos[0]
marca = lista_carro[0]
for i in range(v):
    if lista_litros_gastos[i] < economico:
        economico = lista_litros_gastos[i]
        marca = lista_carro[i]    
    
print("Relatorio final:")
for i in range(v):
    print("%d - %s       - %s - %.1f litros - R$ %.2f"%(cont2,lista_carro[i],lista_consumo[i],lista_litros_gastos[i],lista_preco[i]))
    cont2 +=1
print("O carro mais economico e o %s"%marca)