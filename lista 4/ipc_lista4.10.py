#Beatriz Pessoa Longato 1615310001

a=[] # Vetor que receberá inicialmente os valores

b=[] # Vetor que receberá posterior ao 'a' os valores

c=[] # Vetor que receberá o vetor 'a' + 'b' intercalando valores de cada um

quantidade_elementos=10 # Delimita quantos números deverão ter cada vetor


for i in range(quantidade_elementos): # Enquanto o índice 'i' pertencer ao alcance de 0 até 9, ele irá...
    
    n=float(raw_input("Digite um número para a lista A: ")) # Solicitará valores para n
    
    a.append(n) # Armazenará os valores de 'n' ao vetor 'a'
    
for i in range (quantidade_elementos): # Enquanto o índice 'i' pertencer ao alcance de 0 até 9, ele irá...
    
    n2=float(raw_input("Digite um número para a lista B: ")) # Solicitará valores para n2
    
    b.append(n2) # Armazenará os valores de 'n' ao vetor 'b'
    
for i,y in zip (a,b): # Nesta função aqui (zip), ele intercalará valores de 'a' e 'b' no vetor final 'c'
    
    c.append(i) # Acrescentará os valores respectivos aos índices do vetor 'a' no 'c'
    c.append(y) # Logo após o acima, acrescentará os valores respectivos aos índices do 'b' no 'c'
                # Ou seja, intercalando...
    
print (a) # Imprimirá ao usuário o vetor 'a'
print (b) # Imprimirá ao usuário o vetor 'b'
print "Lista resultante intercalada:"
print (c) # Imprimirá ao usuário o vetor 'c'

    
    











    
    
    

    
