#
#Igor Menezes Sales Vieira - Matricula: 1615310007
#
consoantes = [] # Vetor que receberá todas as consoantes que forem detectadas 
letras = [] # Vetor que receberá todas as letras informadas
acm = 0 # Acumulador que calculará a quantidade de consoantes existentes
for i in range(1,11): # Enquanto i percenter ao intervalo 1 <= i < 11...
    letra = input("Digite letra em aspas:") # ... Solicitará as letras
    letras.append(letra) # FUnção que adicionará 'letra' ao vetor letras
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u": # Se for igual a vogais
        acm = acm # O acumulador permanecerá o mesmo
    else: # Caso não seja vogal
        acm = acm + 1 # Acmulador será acrescido de um
        consoantes.append(letra) # Adicionará a letra ao vetor consoantes

print("%d consoantes foram lidas.\n Elas sao as seguintes: %s"%(acm, consoantes)) # Impressão das consoantes e sua quantidade
