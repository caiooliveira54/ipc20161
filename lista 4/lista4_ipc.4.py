#Beatriz Pessoa Longato 1615310001


vogais = [] # Vetor que servirá para armazenar as vogais informadas

consoantes = [] # Vetor que servirá para armazenar as consoanter informadas

cont = 1 # Contador para ser incrementado durante loopings até a condição ser False

x=0 # Funcionará como um acumulador para as consoantes


while cont <= 10: # Enquanto isso for verdade...
    
    letras = (raw_input("Digite uma letra: ")) #... Solicitará para que o usuário informe uma letra qualquer
    
    
    cont += 1 # Contador que irá incrementar
    
    if letras != "a" or letras != "e" or letras != "i"  or letras != "o"  or letras != "u": # Condição para ser consoante (Substitui os 'And' por 'Or')
        
        consoantes.append(letras) # A cada lopping que for digitado uma consoante, ela será armazenada no vetor 'consoantes'
        
        x +=1 # Acumulador que informará a quantidade de consoantes inseridas
        
    else: # Caso a condição acima não seja verdadeira, cairá nessa e...
        
        vogais.append(letras) #... Adicionará a vogal informada no vetor 'vogais'
          
        

        
print (10-x) , "Vogais" # Irá imprimir o numero de vogais que será a subtração do total menos a quantidade de consoantes (Calculada pelo acumulador)
    
print (vogais) # Irá imprimir o vetor 'vogais'
        

        
print x , "Consoantes"  # Irá imprimir o numero de consoantes
    
print (consoantes) # Irá imprimir o vetor 'consoantes'
