#
#Programa Lista 4, questão 8;
#Felipe Henrique Bastos Costa - 1615310032;
#
idade = []
inverso_i = []
altura = []
inverso_a = []
v = 5
cont1 = 0
cont2 = 1

while(cont1 < v):
    x = int(input("Informe a idade da %dº pessoa:\n"%cont2))
    y = float(input("Informe a altura da %dº pessoa:\n"%cont2))
    idade.append(x)
    altura.append(y)
    cont1 += 1
    cont2 += 1

while(v > 0):
    v-=1
    w = idade[v]
    z = altura[v]
    inverso_i.append(w)
    inverso_a.append(z)
    
print("A ordem inversa das idades e alturas dadas foi:")
print("1.idade = %s"%inverso_i)
print("2.altura = %s"%inverso_a)
