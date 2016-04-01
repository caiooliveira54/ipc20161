#Beatriz Pessoa Longato 1615310001

notas = [] # Vetor onde serão armazenada as notas informadas

quantidade_notas= 4 # Limitador para condição

media = 0 # Média funcionará como acumulador, somará todos os valores informados abaixo do "For"

for i in range (quantidade_notas): # Aqui será realizada uma verificação com 'i' sendo o índice até ele ter 4 índices. (0 - 3)
    
    notas.append(float(raw_input("Digite a nota: "))) # Função que solicitará as notas do usuário enquanto o 'For' for estiver no alcance
    
    media = media + notas[i] # Acumulador das notas informadas acima, ex.: Primeiramente digitel nota 10, ficará no indice i = 0
                             # assim sucessivamente, acumulará as notas que forem digitadas a cada looping
media = media / quantidade_notas # Obviamente pegará o acumulador com todas as 4 notas e dividirá pela quantidade de notas

print (notas) # Irá imprimir a lista 'notas'

print "A média é" , (media) # Irá imprimir a média das notas
