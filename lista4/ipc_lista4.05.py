#Beatriz Pessoa Longato 1615310001

numeros= [] # Lista que armazenará todos os números informados pelo usuário 

par= [] # Lista que armazenará todos os números pares informados pelo usuário 

impar=[] # Lista que armazenará todos os números impares informados pelo usuário 

cont= 1 # Contador para ser utilizado na condição até desobedecer a condição

while cont <= 20: # Enquanto o contador obedecer a condição...
    
    n=int(raw_input("Digite um número: ")) # Solicitará um número ao usuário, e...
    
    numeros.append(n) # ... por consequência armazenado na lista 'numeros'
    
    cont +=1 # Contador sendo incrementado a cada número informado e armazenado
    
    if n % 2 == 0: # Se o resto da divisão do número informado por 2 for zero, será considerado como par...
        
        par.append(n) #... e armazenado na lista 'par'
        
    else: # Caso não seja verdade a condição acima, cairá nesta daqui e será ímpar...
        
        impar.append(n) # ... e armazenado aqui
        
        
print (numeros) # Imprimirá ao usuário o vetor 'numeros'

print(par) # Imprimirá ao usuário o vetor 'par'

print(impar) # Imprimirá ao usuário o vetor 'impar'
    
    
    

