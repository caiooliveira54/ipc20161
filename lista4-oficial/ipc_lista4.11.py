#Lorene Marques - 1615310013
v1 = []
v2 = []
v3 = []
v4 = []
x = 0
print("Primeiro vetor")
for i in range(0,10):
    num1 = input("Informe um elemento: ")
    v1.append(num1)
print("Segundo vetor")
for i in range(0,10):
    num2 = input("Informe um elemento: ")
    v2.append(num2)
print("Terceiro vetor")
for i in range(0,10):
    num3 = input("Informe um elemento: ")
    v3.append(num3)
while x < 10:
    v4.append(v1[x])
    v4.append(v2[x])
    v4.append(v3[x])
    x += 1
print("O vetor intercalado: ")
print(v4)
