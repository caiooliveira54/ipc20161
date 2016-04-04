#
#Programa Lista 4, questão 8;
#Felipe Henrique Bastos Costa - 1615310032;
#
idade = [] # Vetor que armazenará todas as idades inseridas pelo usuário
inverso_i = [] # Vetor que armazenará todas as idades invertidas
altura = [] # Vetor que receberá todas as alturas inseridas pelo usuário
inverso_a = [] # Vetor que receberá todas as alturas invertidas
v = 5 # Limite de pessoas
cont1 = 0
cont2 = 1

while(cont1 < v): # Equanto for menor que 5 solicitará os valores x e y
    x = int(input("Informe a idade da %dº pessoa:\n"%cont2))
    y = float(input("Informe a altura da %dº pessoa:\n"%cont2))
    idade.append(x) # Adicionará x ao vetor idade
    altura.append(y) # Adicionará y ao vetor altura
    cont1 += 1
    cont2 += 1

while(v > 0): # Aqui será invertida as listas idade e altura
    v-=1
    w = idade[v]
    z = altura[v]
    inverso_i.append(w)
    inverso_a.append(z)
    
print("A ordem inversa das idades e alturas dadas foi:")
print("1.idade = %s"%inverso_i)
print("2.altura = %s"%inverso_a)
