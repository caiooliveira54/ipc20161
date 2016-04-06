#
#Programa Lista 4, questão 16;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista1 = []
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
cont1 = 0
cont2 = 1
num_funcionarios = int(input("Informe o numero de funcionarios que trabalham na empresa:\n"))

for k in range(num_funcionarios):
    comis = float(input("Qual o valor das vendas brutas do %dº funcionario?:\n"%cont2))
    lista1.append(comis)
    salario = 200 + 9*comis/100
    if(salario >= 200 and salario < 300):
        a += 1
    if(salario >= 300 and salario < 400):
        b += 1
    if(salario >= 400 and salario < 500):
        c += 1
    if(salario >= 500 and salario < 600):
        d += 1
    if(salario >= 600 and salario < 700):
        e += 1
    if(salario >= 700 and salario < 800):
        f += 1
    if(salario >= 800 and salario < 900):
        g += 1
    if(salario >= 900 and salario < 1000):
        h += 1
    if(salario >= 1000):
        i += 1
    cont2 += 1
print(a,b,c,d,e,f,g,h,i)