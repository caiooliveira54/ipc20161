#Nickso Patrick Façanha Calheiros - 1615310059

vet = []
par = []
impar = []
cont = 0

while cont < 20:
    numero = int(input("digite um numero: "))
    vet.append (numero)
    if numero%2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
    cont = cont + 1
print ("Numeros do vetro impar", impar)
print ("Numeros do vetor par", par)
print ("Todos os numeros digitados", vet)
    
    
