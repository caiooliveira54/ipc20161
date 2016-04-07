#
#Igor Menezes Sales Vieira - Matricula: 1615310007
#
idade = [] # Vetor que receberá todas as idades informadas
altura = [] # Vetor que receberá todas as alturas informadas
idadeinv = [] # Vetor que receberá os elementos do vetor idade de forma invertida
alturainv = [] # Vetor que receberá os elementos do vetor altura de forma invertida

for i in range(1,6): 
    idadex = int(input("Idade: ")) # Usuario informara as idades
    alturax = float(input("Altura: ")) # Usuario inforara as alturas
    idade.append(idadex) # Adicionara através da funçao as idades informadas ao vetor idade
    altura.append(alturax) # Adicionara através da funçao as alturas informadas ao vetor altura

i = len(idade) - 1 # Contador com o número igual ao índice do último elemento do vetor idade
while i >= 0:  # Enquanto i estiver nesta condição
    idadeinv.append(idade[i]) # Pegará o numero no índice i do vetor idade e colocara no vetorinv
    i = i-1 # Decrementando o contador

i = len(altura) -1 # Contador com o número igual ao índice do último elemento do vetor altura
while i >= 0: # Enquanto i estiver nesta condição
    alturainv.append(altura[i]) # Pegará o numero no índice i do vetor alturas e colocara no vetor alturainv
    i = i-1 # Decrementando o contador

print(idadeinv)
print(alturainv)
    
