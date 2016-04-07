#
#Igor Menezes Sales Vieira - Matricula: 1615310007
#
notas = [] # Vetor que receberá todas as notas informadas
acm = 0 # Acumulador que fará a soma de todas as notas

for i in range(1,5): # Enquanto estiver no alcance de 1-4 solicitará valores ao usuário
    notaind = float(input("Informe a nota: ")) 
    notas.append(notaind) # Adicionará a nota ao vetor notas
    acm = acm + notaind # Acumulará as notas

media = acm / i # Média vai ser igual ao acumulador que são todas as notas sobre o 'i' que o índice 4 
for i in notas: # Imprimirá todas as notas conforme for realizando iterações
    print("Notas:%.1f"%i)
print("A media e %.1f"%media) # Imprimirá a média
