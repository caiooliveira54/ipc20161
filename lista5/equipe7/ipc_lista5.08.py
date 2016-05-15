#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033


def calcular_fatorial(num):
    if (num ==1) or (num ==0):
        return 1
    else:
        return num * calcular_fatorial(num-1)

def analisar_combinacao(num, i):
    ac= calcular_fatorial(num)/(calcular_fatorial(i) * calcular_fatorial(num - i))
    return ac

num = int (input("Qual o numero limite? "))
vet = []
for num in range(0,num + 1):
	triangulo = []
	for i in range(0,num + 1):
		triangulo.append(int(analisar_combinacao(num,i)))
		vet.append(int(analisar_combinacao(num,i)))
	print(triangulo)
print(vet)