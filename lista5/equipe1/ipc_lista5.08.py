#Introducao a programacao de computadores
#Professor: Jucimar Junior
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Nahan Trindade Passos - 1615310021

def fatorar(num):
    if (num == 1) or (num == 0):
        return 1
    else:
        return num * fatorar(num-1)

def anal_comb(num, i):
    ac = fatorar(num) / (fatorar(i) * fatorar(num - i))
    return ac

num = int (input ("Qual o limite? "))

for num in range(0, num+1):
    triangulo = []
    for i in range(0, num+1):
        triangulo.append(int(anal_comb(num, i)))
    print (triangulo)
