# Mateus Mota de Souza - 1615310016
num = 0
numeros = []
numeros_i = []
soma = 0
acm = 0
acm2 = 0
ultimo = len(numeros)-1

while num != -1:
    num = int(input("Insira um numero (Para parar digite -1): "))
    numeros.append(num)
    if num == -1:
        del(numeros[-1])        
    soma += num
    tamanho = len(numeros)
    media = soma/tamanho
for i in numeros:
    if i > media:
        acm += 1
    if i < 7:
        acm2 += 1
for i in range(tamanho):
    numeros_i.append(numeros[ultimo])
    ultimo -= 1    

print ("\nO tamanho da lista é:", tamanho)
print ("Vetor =", numeros)
print ("Vetor invertido =", numeros_i)
print ("A media dos valores é:", media)
print ("Quantidade de números acima da média:", acm)
print ("Quantidade de números menores que sete:", acm2)
print ("Isto é tudo pessoal!")
    
