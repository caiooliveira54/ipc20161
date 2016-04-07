#
#Igor Menezes Sales Vieira - Matricula: 1615310007
#
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # Numeros que serão verificados se são impares ou pares
vetor_par = [] # Vetor que receberá os números que forem pares
vetor_impar = [] # Vetor que receberá os números que forem ímpares
v = len(numeros) # Quantidade de termos no vetor numeros

for i in numeros: # Enquanto estiver percorrendo o vetor numeros
    if(numeros[i] % 2 == 0): # Se o resto da divisão do número por 2 for zero, será par
        vetor_par.append(numeros[i]) # E em seguida adicionado ao vetor par
    else: # Caso não for
        vetor_impar.append(numeros[i]) # Será automaticamente mandado para o vetor impar
   
print("Primeiro vetor = ",numeros) ####
print("Vetor par = ",vetor_par)       # Impressão dos vetores numeros, pares e impares
print("Vetor impar = ",vetor_impar)####
