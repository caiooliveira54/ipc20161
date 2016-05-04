#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Kid Mendes de Oliveira Neto - 1615310011
#Eduardo Maia Freire - 1615310003
#Igor Menezes Sales Vieira - 1615310007
#

def fatorial(n):                                        #Fatoração Numérica
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n-1)

def analise_c(n,i):                                     #Análise Combinatória
    ac = fatorial(n)/(fatorial(i)*fatorial(n-i))
    return ac


n = int(input("Digite um valor de n:\n"))               #Entrada
vetor = []

for n in range(0,n+1):                                  #Processamento
    vet = []
    for i in range(0,n+1):
        vet.append(int(analise_c(n,i)))
        vetor.append(int(analise_c(n,i)))
    print(vet)                                          #Triângulo de Pascal
print(vetor)                                            #Triângulo de Pascal apenas em um vetor
        
    
    

