#Beatriz Pessoa Longato 1615310001

cont=1 # Contador definido para ser usado como condição
x=10 # x Atuará como um limite para um contador
L= [] # Vetor vazio que receberá os valores informados

while cont <= x: # Enquanto isso for verdade...
    L.append(int(raw_input("Digite um número: "))) # ... Solicitará um número ao usuário
    
    cont +=1 # Contador incrementado para evitar loopings
    
print (L)   # Impressão do vetor com os números informados pelo usuário

print (list(reversed(L))) # Impressão do inverso através de função (Dica: Rever, pois o professor quer uma lógica para isso. Obs.: Considerado 'cheat')
