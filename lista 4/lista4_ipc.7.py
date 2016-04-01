#Beatriz Pessoa Longato 1615310001

numeros=[] # Vetor que armazenará o todos os números informados pelo usuário

quant_numero= 5 # Variável que será usada na condição e delimita a quantidade de números a ser informada

soma=0 # Acumulador que irá fazer a soma de todos os 5 valores informados

mult=1 # Acumulador que irá realizar as multiplicaçoes sucessivas dos números informados ('mult = 1' pois o 1 é o elemento neutro da multiplicação)

for i in range (quant_numero): # Enquanto 'i' que é o índice pertencer ao vetor que vai de 0 até 4...
 
    n=int(raw_input("Digite um número: ")) # ... Solicitará um valor do usuário...
    
    numeros.append(n) # ... Que será armazenado no vetor 'numeros'
    
    soma= soma + numeros[i] # ... O acumulador 'soma' pegará tal número informado e somará com os posteriores e armazenará até o final quando tiver todos os números nele
    
    mult = mult * numeros[i] # ... O acumulador 'mult' pegará tal número informado e multiplicará pelo próximo informado até o final quando tiver todos os números nele
    
print (numeros) # Imprimirá ao usuário o vetor 'numeros' com todos os números informados pelo usuário

print (soma) # Imprimirá o resultado final do acumulador que será a soma dos cinco termos

print (mult) # Imprimirá o resultado final do acumulador que será a multiplicação dos cinco termos


    
    
    
    
    
    
