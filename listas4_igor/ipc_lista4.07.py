#
#Igor Menezes Sales Vieira - Matricula: 1615310007
#
vetor = [] # Vetor que receberá todos os valores
multiplicacao = 1 # Acumulador multiplicação inicialmente 1 pois 1 é o número neutro da multiplicação
soma = 0 # Acumulador soma = 0

for i in range(1,6): 
    dado = int(input("Digite o dado: ")) # Solicitará elementos enquanto estiver no alcance
    vetor.append(dado) # O número informado será acrescentado ao vetor
    multi = multiplicacao * dado # o numero informado será multiplicado por 1 e pelos pŕóximos numeros informados
    soma = soma + dado # o numero informado sera acumulado com os valores anteriores e os posteriores

print("O numeros informados foram: ",vetor) ##
print("A soma:%d"%soma)                      # Impressão do vetor, da multiplicação dos termos e da soma dos termos
print("A multiplicacao:%d"%multiplicacao)   ##
