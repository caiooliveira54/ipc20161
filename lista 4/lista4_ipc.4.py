#Beatriz Pessoa Longato 1615310001


vogais = []

consoantes = []

cont = 1

x=0


while cont <= 10:
    
    letras = (raw_input("Digite uma letra: "))
    
    
    cont += 1
    
    if letras != "a" and letras != "e" and letras != "i"  and letras != "o"  and letras != "u":
        
        consoantes.append(letras)
        
        x +=1 
        
    else:
        
        vogais.append(letras)
          
        

        
print (10-x) , "Vogais"
    
print (vogais)
        

        
print x , "Consoantes" 
    
print (consoantes)
