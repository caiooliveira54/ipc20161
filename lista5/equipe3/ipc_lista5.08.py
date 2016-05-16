#Introducao a programacao de computadores
#Professor: Jucimar Junior
#samuel silva de frança - 1615310049
#bruno de oliveira freire - 1615310030
#Felipe Henrique Bastos Costa - 1615310032
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
