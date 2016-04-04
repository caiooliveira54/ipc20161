# Nickso Patrick Façanha Calheiros
A =[1,2,3,4,5,6,7,8,9,10]
cont = 0
ind = len(A)
soma = 0

while cont < ind:
    quadrado = A[cont]**2
    soma = quadrado + soma
    cont = cont + 1
print ("A Soma dos quadrados dos termos é:",soma)
