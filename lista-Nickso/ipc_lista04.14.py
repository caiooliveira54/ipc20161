l = list(range(5))
p = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhoe com a vítima?"]
x = 0
ac_s = 0
v = len(l)

while x < v:
    l[x] = input("%s(Digite S para sim ou N para não):" % (p[x]))
    if l[x] != "s" and l[x] != "n":
        print ("Erro - Resposta invalida")
        del l[x]
        l[x] = input("%s(Digite S para sim ou N para não):" % p[x])

    if l[x] == "s" :
        ac_s += 1
    x += 1
if ac_s == 2:
    print ("Suspeito")
if ac_s == 3 or ac_s == 4:
    print ("Cumplice")
if ac_s == 5:
    print ("Assassino")
if ac_s == 1 or ac_s == 0:
    
    print ("Inocente")
