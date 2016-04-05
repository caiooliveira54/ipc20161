#Eduardo Maia Freire lista4 questao 9
vetor_A = [1,2,3,4,5,6,7,8,9,10]
x = 0
v = len(vetor_A)
quadrado = 0
soma_quadrado = 0
for x in range (v):
    quadrado =(vetor_A[x])**2
    quadrado2 = (vetor_A[x-1])**2
    soma_quadrado = quadrado + quadrado2
    x = x + 1
    print(quadrado)
print("Soma dos quadrados = ",soma_quadrado)
