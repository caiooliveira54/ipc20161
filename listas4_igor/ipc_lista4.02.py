#
#Igor Menezes Sales Vieira - Matricula: 1615310007
#
vetor1 = [] # Vetor que receberá os primeiros valores informados pelo usuário
vetor2 = [] # Vetor que receberá o vetor1 na ordem inversa

for i in range(1,6): # Enquanto estiver no alcance de 1 até 5 solicitará valores ao usuário
    num = int(input("Digite numero:"))
    vetor1.append(num) # Função que adiciona os números acima informados ao vetor1

i = len(vetor1) - 1 # Representação do índice do último elemento para pegá-lo e jogá-lo no primeiro indice do vetor2 
while i >= 0:
    indice = vetor1[i] 
    vetor2.append(indice)
    i = i - 1 # Decremento do i para que passe para o penúltimo, depois para o antepenultimo até o i = 1 e pegar o primeiro elemento do vetor 1
print(vetor2) # Impressão do vetor1 invertido

