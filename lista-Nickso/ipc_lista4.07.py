vetor = [1,2,3,4,5]
cont = 0
ind = len(vetor)
soma = 0
mult = 1

while cont < ind:
    soma = vetor[cont] + soma  
    mult = vetor[cont] * mult    
    cont = cont + 1
print (vetor)    
print (soma)
print (mult)
    
    
