saltos = []
sequencia = ["Primeiro","Segundo","Terceiro","Quarto","Quinta"]
media = 0
acm = 0

nome = raw_input("Atleta: ")
print("")
for i in range(5):
    salto = float(input("%s Salto:"%sequencia[i]))
    saltos.append(salto)
    acm = acm + salto

media = acm / 5
print("Resultado Final:",nome,salto,media)