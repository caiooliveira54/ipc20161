temperatura = []
acm = 0
for i in range(12):
    tempx = float(input("Digite a temperatura do mes%d: "%(i+1)))
    temperatura.append(tempx)
    acm = acm + tempx

media = acm/12

for i in range(12):
    if temperatura[i] > media:
        print(temperatura[i], i+1)

print(media)

