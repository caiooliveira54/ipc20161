#Beatriz Pessoa Longato 1615310001

A=[] # Vetor definido como A e que receberá os números informados pelo usuário

quantidade_num= 10 # Variável que determina a quantidade de números a serem informados

soma= 0 # Acumulador que fará o somatórios de todos os números


for i in range (quantidade_num): # Enquanto o índice i pertencer estiver ao alcance de 'quantidade_num', ou seja, intervalo 0 <= i <10...
    
    num=int(raw_input("Digite um número: ")) # Solicitará ao usuário um valor inteiro
    
    A.append(num) # O valor informado acima pelo usuário será armazenado no vetor 'A' 
    
    quad= num * num # Aqui realizará o quadrado do número informado acima e...
    
    soma= soma + quad # ... Aqui será somado no acumulador com os próximos valores
    
    
print (A) # Imprimirá o vetor 'A'


print (soma) # Imprimirá a soma dos quadrados dos números do vetor 'A'

    
    
    
    
    
    
             
             
